<template>
    <div class="container mt-5">
        <h1 class="text-center mb-4">
          Available Positions
        </h1>

        <div v-if="loadError" class="alert alert-danger" role="alert">
            {{ loadError }}
        </div>

        <div v-if="ratingError" class="alert alert-danger" role="alert">
            {{ ratingError }}
        </div>

        <div
            v-if="ratingMessage"
            class="alert alert-success"
        >
            {{ ratingMessage }}
        </div>

        <div class="mb-4">
            <label for="position-search" class="form-label">
                Search volunteer positions
            </label>

            <input
                id="position-search"
                v-model="searchKeyword"
                type="search"
                class="form-control"
                placeholder="Search title or description"
                @input="filterPositions"
            >

            <p class="small mt-2" role="status">
                {{ filteredPositions.length }} matching position(s).
            </p>
        </div>

        <OpportunityMap :matching-positions="filteredPositions" />
        
        <div class="row">
            <div
                v-for="position in filteredPositions"
                :key="position.id"
                class="col-12 col-sm-6 col-lg-4 col-xxl-3 mb-4"
            >
                <div class="card h-100">
                    <div class="card-body">
                        <h2 class="card-title h5">
                            {{ position.title }}
                        </h2>

                        <p class="card-text">
                            <strong>Location:</strong>
                            {{ position.location }}
                        </p>

                        <p class="card-text">
                            {{ position.description }}
                        </p>

                        <p>
                            <strong>Average rating: </strong>

                            <span v-if="position.ratings.length > 0">
                                {{ averageRating(position) }} / 5
                                from {{ position.ratings.length }} user(s)
                            </span>

                            <span v-else>
                                No ratings yet
                            </span>
                        </p>

                        <label
                            :for="'rating-' + position.id"
                            class="form-label"
                        >
                            Your rating
                        </label>

                        <select
                            :id="'rating-' + position.id"
                            v-model.number="position.selectedRating"
                            class="form-select mb-3"
                            :disabled="isRating"
                        >
                            <option disabled value="">
                                Select a rating
                            </option>

                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>

                        <button
                            type="button"
                            class="btn btn-primary"
                            @click="submitRating(position)"
                            :disabled="isRating"
                        >
                            Submit Rating
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import { currentUser } from '../auth.js'
    import { positions, loadPositions } from '../positions.js'
    import { doc, setDoc } from 'firebase/firestore';
    import { db } from '../firebase/init.js';
    import OpportunityMap from '../components/OpportunityMap.vue'; 

    const ratingMessage = ref('') //successful rating feedback
    const ratingError = ref(''); //rating failure feedback
    const isRating = ref(false); //prevent overlapping rating
    const loadError = ref(''); //loading failure feedback
    const searchKeyword = ref(''); //store text in searchbar
    const filteredPositions = ref([]); //job in card that will pass to map

    const filterPositions = () => {
        const keyword = searchKeyword.value.trim().toLowerCase();

        filteredPositions.value = positions.value.filter((position) => {
            return !position.archived && (
                position.title.toLowerCase().includes(keyword)
                || position.description.toLowerCase().includes(keyword)
            );
        });
    };

    onMounted(async () => {
        try {
            await loadPositions();
            filterPositions();
        } catch (error) {
            console.error('Loading positions failed:', error);
            loadError.value = 'Could not load positions.';
        }
    });

    const submitRating = async (position) => {
        if (isRating.value) return;

        ratingMessage.value = '';
        ratingError.value = '';

        const score = Number(position.selectedRating);

        if (!Number.isInteger(score) || score < 1 || score > 5) {
            ratingError.value = 'Please select a rating from 1 to 5.';
            return;
        }

        if (!currentUser.value) {
            ratingError.value = 'Please log in before rating.';
            return;
        }

        const userId = currentUser.value.id;
        isRating.value = true;

        try {
            await setDoc(
                doc(db, 'positions', position.id, 'ratings', userId),
                { score: score }
            );

            const matchingRatings = position.ratings.filter((rating) => {
                return rating.userId === userId;
            });

            if (matchingRatings.length > 0) {
                matchingRatings[0].score = score;
            } else {
                position.ratings.push({
                    userId: userId,
                    score: score,
                });
            }

            position.selectedRating = '';
            ratingMessage.value =
                'Your rating for ' + position.title + ' has been saved.';
                
        } catch (error) {
            console.error('Saving rating failed:', error);
            ratingError.value = 'Could not save your rating. Please try again.';
        } finally {
            isRating.value = false;
        }
    };

    const averageRating = (position) => {
        if (position.ratings.length === 0) {
            return 0
        }

        let total = 0

        position.ratings.forEach((rating) => {
            total = total + rating.score
        })

        return total / position.ratings.length
    }
</script>