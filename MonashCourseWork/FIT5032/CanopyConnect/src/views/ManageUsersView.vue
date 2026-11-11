<template>
    <div class="container mt-5">
        <h1 class="text-center">Manage Registered Users</h1>

        <p class="text-center">
            View registered user profiles.
        </p>

        <div v-if="loadError" class="alert alert-danger" role="alert">
            {{ loadError }}
        </div>

        <div v-if="successMessage" class="alert alert-success" role="status">
            {{ successMessage }}
        </div>

        <div v-if="updateError" class="alert alert-danger" role="alert">
            {{ updateError }}
        </div>

        <DataTable
            :value="users"
            dataKey="id"
            paginator
            :rows="10"
            stripedRows
            tableStyle="min-width: 40rem"
            v-model:filters="filters"
            filterDisplay="row"
        >
            <template #empty>No user profiles found.</template>

            <Column field="username" header="Username" sortable :showFilterMenu="false">
                <template #filter="slotProps">
                    <input
                        v-model="slotProps.filterModel.value"
                        type="text"
                        class="form-control"
                        placeholder="Search username"
                        aria-label="Search by username"
                        @input="slotProps.filterCallback()"
                    >
                </template>
            </Column>

            <Column field="role" header="Current role" sortable :showFilterMenu="false">
                <template #filter="slotProps">
                    <input
                        v-model="slotProps.filterModel.value"
                        type="text"
                        class="form-control"
                        placeholder="Search role"
                        aria-label="Search by role"
                        @input="slotProps.filterCallback()"
                    >
                </template>
            </Column>

            <Column field="email" header="Email" sortable :showFilterMenu="false">
                <template #filter="slotProps">
                    <input
                        v-model="slotProps.filterModel.value"
                        type="text"
                        class="form-control"
                        placeholder="Search email"
                        aria-label="Search by email"
                        @input="slotProps.filterCallback()"
                    >
                </template>
            </Column>

            <Column header="Change role">
                <template #body="slotProps">
                    <select
                        :value="slotProps.data.role"
                        class="form-select"
                        :disabled="!currentUser || slotProps.data.id === currentUser.id || savingUserId !== ''"
                        :aria-label="'Change role for ' + slotProps.data.username"
                        @change="changeRole(slotProps.data, $event)"
                    >
                        <option value="viewer">Viewer</option>
                        <option value="editor">Editor</option>
                        <option value="admin">Admin</option>
                    </select>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { db } from '../firebase/init.js';
    import { collection, getDocs, doc, updateDoc } from 'firebase/firestore';
    import { currentUser } from '../auth.js';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import { FilterMatchMode } from '@primevue/core/api';
    
    const users = ref([]);
    const loadError = ref('');
    const successMessage = ref('');
    const updateError = ref('');
    const savingUserId = ref('');

    const filters = ref({
        username: { value: null, matchMode: FilterMatchMode.CONTAINS },
        role: { value: null, matchMode: FilterMatchMode.CONTAINS },
        email: { value: null, matchMode: FilterMatchMode.CONTAINS },
    });

    onMounted(async () => {
        try {
            const snapshot = await getDocs(collection(db, 'users'));
            users.value = snapshot.docs.map((document) => {
                return{
                    id: document.id,
                    username: document.data().username,
                    email: document.data().email,
                    role: document.data().role,
                };
            });
        } catch (error) {
            console.error('Loading user failed:', error);
            loadError.value = 'Could not load user profiles.';
        }
    })

    const changeRole = async (user, event) => {
        const select = event.target;
        const newRole = select.value;

        if (!currentUser.value || savingUserId.value) return;
        if (user.id === currentUser.value.id) return;

        successMessage.value = '';
        updateError.value = '';
        savingUserId.value = user.id;

        try {
            await updateDoc(doc(db, 'users', user.id), {
                role: newRole,
            });

            user.role = newRole;
            successMessage.value =
                user.username + ' now has the ' + newRole + ' role.';
        } catch (error) {
            select.value = user.role;
            console.error('Updating role failed:', error);
            updateError.value = 'Could not save the role change.';
        } finally {
            savingUserId.value = '';
        }
    };
</script>