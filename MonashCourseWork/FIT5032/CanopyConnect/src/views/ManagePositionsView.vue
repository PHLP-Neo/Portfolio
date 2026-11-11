<template>
    <div class="container mt-5">
        <h1 class="text-center">Manage Positions</h1>
        
        <div v-if="loadError" class="alert alert-danger" role="alert">
            {{ loadError }}
        </div>

        <p v-if="editingPosition" class="text-center">
            Update the selected community position.
        </p>

        <p v-else class="text-center">
            Add a new community position.
        </p>
    
        <div v-if="successMessage" class="alert alert-success" role="status">
            {{ successMessage }}
        </div>
    
        <div class="row justify-content-center">

            <div v-if="saveError" class="alert alert-danger" role="alert">
                {{ saveError }}
            </div>

            <form 
                class="col-12 col-md-10 col-lg-8 col-xl-7 col-xxl-6 mt-4"
                @submit.prevent="submitPosition"
            >
                <div class="mb-3">
                    <label for="position-title" class="form-label">
                        Position title
                    </label>
            
                    <input
                        id="position-title"
                        v-model="formData.title"
                        type="text"
                        class="form-control"
                        :aria-invalid="Boolean(errors.title)"
                        aria-describedby="position-title-error"
                        @blur="() => validateTitle(true)"
                        @input="() => validateTitle(false)"
                        required
                    >
            
                    <div id="position-title-error" class="text-danger" aria-live="polite">
                        {{ errors.title }}
                    </div>
                </div>
        
                <div class="mb-3">
                    <label for="position-location" class="form-label">
                        Location
                    </label>
            
                    <input
                        id="position-location"
                        v-model="formData.location"
                        type="text"
                        class="form-control"
                        :aria-invalid="Boolean(errors.location)"
                        aria-describedby="position-location-error"
                        @blur="() => validateLocation(true)"
                        @input="() => validateLocation(false)"
                        required
                    >
            
                    <div id="position-location-error" class="text-danger" aria-live="polite">
                        {{ errors.location }}
                    </div>
                </div>
        
                <div class="mb-3">
                    <label for="position-description" class="form-label">
                        Description
                    </label>
            
                    <textarea
                        id="position-description"
                        v-model="formData.description"
                        class="form-control"
                        rows="4"
                        :aria-invalid="Boolean(errors.description)"
                        aria-describedby="position-description-error"
                        @blur="() => validateDescription(true)"
                        @input="() => validateDescription(false)"
                        required
                    ></textarea>
            
                    <div id="position-description-error" class="text-danger" aria-live="polite">
                        {{ errors.description }}
                    </div>
                </div>
        
                <div class="d-grid gap-2 d-sm-flex">

                    <button
                        v-if="editingPosition"
                        type="submit"
                        class="btn btn-primary"
                        :disabled="isSaving"
                    >
                        Update Position
                    </button>

                    <button
                        v-else
                        type="submit"
                        class="btn btn-primary"
                        :disabled="isSaving"
                    >
                        Add Position
                    </button>
            
                    <button
                        type="button"
                        class="btn btn-secondary"
                        @click="clearForm"
                        :disabled="isSaving"
                    >
                        Clear
                    </button>
                </div>
            </form>
        </div>

        <hr class="my-5">

        <h2>Existing Positions</h2>

        <button
            type="button"
            class="btn btn-outline-success mb-3"
            :disabled="positions.length === 0"
            @click="exportPositions"
        >
            Export Positions CSV
        </button>

        <DataTable
            :value="positions"
            dataKey="id"
            paginator
            :rows="10"
            stripedRows
            tableStyle="min-width: 40rem"
            v-model:filters="filters"
            filterDisplay="row"
            ref="positionsTable"
            exportFilename="canopy-positions"
        >
            <template #empty>No positions found.</template>

            <Column field="title" header="Title" sortable :showFilterMenu="false">
                <template #filter="rowDetails">
                    <input
                        v-model="rowDetails.filterModel.value"
                        type="text"
                        class="form-control"
                        placeholder="Search title"
                        aria-label="Search by position title"
                        @input="rowDetails.filterCallback()"
                    >
                </template>
            </Column>

            <Column field="location" header="Location" sortable :showFilterMenu="false">
                <template #filter="rowDetails">
                    <input
                        v-model="rowDetails.filterModel.value"
                        type="text"
                        class="form-control"
                        placeholder="Search location"
                        aria-label="Search by location"
                        @input="rowDetails.filterCallback()"
                    >
                </template>
            </Column>

            <Column header="Action" :exportable="false">
                <template #body="rowDetails">
                    <div class="d-flex flex-column flex-lg-row gap-2 align-items-start">
                        <button
                            type="button"
                            class="btn btn-outline-primary btn-sm text-nowrap"
                            :disabled="isSaving"
                            :aria-label="'Edit ' + rowDetails.data.title"
                            @click="startEditing(rowDetails.data)"
                        >
                            Edit
                        </button>

                        <button
                            type="button"
                            class="btn btn-sm text-nowrap"
                            :class="rowDetails.data.archived
                                ? 'btn-outline-success'
                                : 'btn-warning'"
                            :disabled="isSaving"
                            :aria-label="(rowDetails.data.archived ? 'Restore ' : 'Archive ')
                                + rowDetails.data.title"
                            @click="toggleArchive(rowDetails.data)"
                        >
                            {{ rowDetails.data.archived ? 'Restore' : 'Archive' }}
                        </button>
                    </div>
                </template>
            </Column>
        </DataTable>

    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { positions, loadPositions } from '../positions.js';
    import { collection, addDoc, doc, updateDoc } from 'firebase/firestore';
    import { db } from '../firebase/init.js';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import { FilterMatchMode } from '@primevue/core/api';

    const successMessage = ref('');
    const saveError = ref('');
    const isSaving = ref(false);
    const editingPosition = ref(null)
    const loadError = ref('');
    const positionsTable = ref(null);

    const formData = ref({
        title: '',
        location: '',
        description: '',
    });

    const filters = ref({
            title: { value: null, matchMode: FilterMatchMode.CONTAINS },
            location: { value: null, matchMode: FilterMatchMode.CONTAINS },
        });

    const errors = ref({
        title: '',
        location: '',
        description: '',
    });

    const exportPositions = () => {
        positionsTable.value.exportCSV();
    };

    onMounted(async () => {
        try {
            await loadPositions();
        } catch (error) {
            console.error('Loading positions failed:', error);
            loadError.value = 'Could not load positions.';
        }
    });

    const toggleArchive = async (position) => {
        if (isSaving.value) return;

        successMessage.value = '';
        saveError.value = '';

        const archived = !position.archived;
        isSaving.value = true;

        try {
            await updateDoc(
                doc(db, 'positions', position.id),
                { archived: archived }
            );

            position.archived = archived;

            successMessage.value = archived
                ? 'The position has been archived.'
                : 'The position is available again.';
        } catch (error) {
            console.error('Changing position availability failed:', error);
            saveError.value = 'Could not change position availability.';
        } finally {
            isSaving.value = false;
        }
    };

    const submitPosition = async () => {
        if (isSaving.value) return;

        successMessage.value = '';
        saveError.value = '';

        validateTitle(true);
        validateLocation(true);
        validateDescription(true);

        if (
            errors.value.title ||
            errors.value.location ||
            errors.value.description
        ) {
            return;
        }

        const data = {
            title: formData.value.title.trim(),
            location: formData.value.location.trim(),
            description: formData.value.description.trim(),
        }

        const positionToEdit = editingPosition.value;
        isSaving.value = true;

        try {
            if (positionToEdit) {
                await updateDoc(
                    doc(db, 'positions', positionToEdit.id),
                    data
                );

                positionToEdit.title = data.title;
                positionToEdit.location = data.location;
                positionToEdit.description = data.description;
            } else {
                const reference = await addDoc(
                    collection(db, 'positions'),
                    data
                );

                positions.value.push({
                    id: reference.id,
                    title: data.title,
                    location: data.location,
                    description: data.description,
                    ratings: [],
                    selectedRating: '',
                });
            }

            clearForm();

            if (positionToEdit) {
                successMessage.value = 'The position has been updated.';
            } else {
                successMessage.value = 'The new position has been added.';
            }
        } catch (error) {
            console.error('Saving position failed:', error);
            saveError.value = 'Could not save the position. Please try again.';
        } finally {
            isSaving.value = false;
        }
    };
    

    const startEditing = (position) => {
        editingPosition.value = position;

        formData.value = {
            title: position.title,
            location: position.location,
            description: position.description,
        };

        errors.value.title = '';
        errors.value.location = '';
        errors.value.description = '';
        successMessage.value = '';
    }

    const clearForm = () => {
        formData.value = {
            title: '',
            location: '',
            description: '',
        };

        errors.value.title = '';
        errors.value.location = '';
        errors.value.description = '';
        successMessage.value = '';
        editingPosition.value = null;
    }

    const validateTitle = (blur) => {
        if (!formData.value.title.trim()) {
            if (blur) {
            errors.value.title = 'Position title must not be empty.';
            }
        } else {
            errors.value.title = '';
        }
    }

    const validateLocation = (blur) => {
        if (!formData.value.location.trim()) {
            if (blur) {
            errors.value.location = 'Location must not be empty.';
            }
        } else {
            errors.value.location = '';
        }
    }

    const validateDescription = (blur) => {
        if (!formData.value.description.trim()) {
            if (blur) {
            errors.value.description = 'Description must not be empty.';
            }
        } else {
            errors.value.description = '';
        }
    }
</script>

