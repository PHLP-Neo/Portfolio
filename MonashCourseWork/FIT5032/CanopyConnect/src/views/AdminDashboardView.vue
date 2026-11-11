<template>
    <div class="container mt-5">
        <h1>Admin Dashboard</h1>
        <p>Overview of Canopy Connect.</p>

        <div v-if="loadError" class="alert alert-danger" role="alert">
            {{ loadError }}
        </div>

        <div class="row">
            <div class="col-12 col-md-6 col-lg-4 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h2 class="h5">Available positions</h2>

                        <p class="display-6" role="status">
                            {{ isLoading ? 'Loading…' : positionCount ?? '—' }}
                        </p>
                    </div>
                </div>
            </div>

            <div class="col-12 col-md-6 col-lg-4 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h2 class="h5">Registered users</h2>

                        <p class="display-6" role="status">
                            {{ isLoading ? 'Loading…' : userCount ?? '—' }}
                        </p>
                    </div>
                </div>
            </div>

            <div class="col-12 col-md-6 col-lg-4 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h2 class="h5">Archived positions</h2>

                        <p class="display-6" role="status">
                            {{ isLoading ? 'Loading…' : archivedCount ?? '—' }}
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <section class="mb-4" aria-labelledby="user-role-heading">
            <h2 id="user-role-heading" class="h5">Users by role</h2>

            <p v-if="isLoading" role="status">Loading user roles…</p>

            <dl v-else class="row">
                <div
                    v-for="role in userRoles"
                    :key="role"
                    class="col-12 col-sm-4"
                >
                    <dt class="text-capitalize">{{ role }}</dt>
                    <dd>{{ roleCounts[role] }}</dd>
                </div>
            </dl>
        </section>

        <section
            v-if="chartData"
            class="mb-4"
            aria-labelledby="location-chart-heading"
        >
            <h2 id="location-chart-heading" class="h5">
                Positions by location
            </h2>

            <div class="mb-3">
                <label for="chart-status" class="form-label">
                    Position availability
                </label>

                <select
                    id="chart-status"
                    v-model="chartStatus"
                    class="form-select"
                    :disabled="isLoading"
                    @change="updateChart"
                >
                    <option value="available">Available</option>
                    <option value="archived">Archived</option>
                    <option value="all">All positions</option>
                </select>
            </div>

            <p v-if="chartData.labels.length === 0">
                No positions match this filter.
            </p>

            <template v-else>
                <Chart
                    type="bar"
                    :data="chartData"
                    :options="chartOptions"
                    :canvasProps="{
                        role: 'img',
                        'aria-label': chartStatus + ' positions grouped by location'
                    }"
                    style="height: 360px"
                />

                <ul class="small mt-3">
                    <li
                        v-for="location in Array.from(locationCounts.keys())"
                        :key="location"
                    >
                        {{ location }}: {{ locationCounts.get(location) }} position(s)
                    </li>
                </ul>
            </template>
        </section>

        <button
            type="button"
            class="btn btn-outline-primary"
            :disabled="isLoading"
            @click="loadDashboard"
        >
            Refresh
        </button>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
    import { collection, getDocs } from 'firebase/firestore';
    import { db } from '../firebase/init.js';
    import Chart from 'primevue/chart';

    const positionCount = ref(null);
    const userCount = ref(null);
    const archivedCount = ref(null);
    const locationCounts = ref(new Map());
    const loadError = ref('');
    const isLoading = ref(false);

    const userRoles = ['viewer', 'editor', 'admin'];
    const roleCounts = ref({
        viewer: 0,
        editor: 0,
        admin: 0,
    });

    const chartData = ref(null);
    const chartPositions = ref([]);
    const chartStatus = ref('available');
    const chartOptions = {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false,
            },
        },
        scales: {
            x: {
                beginAtZero: true,
                ticks: {
                    precision: 0,
                },
            },
        },
    };

    const updateChart = () => {
        const matchingPositions = chartPositions.value.filter((position) => {
            if (chartStatus.value === 'available') {
                return position.archived !== true;
            }

            if (chartStatus.value === 'archived') {
                return position.archived === true;
            }

            if (chartStatus.value === 'all') {
                return true;
            }

            return false;
        });

        //const locationCounts = new Map();
        locationCounts.value = new Map();

        matchingPositions.forEach((position) => {
            const location = position.location.trim();
            const count = locationCounts.value.get(location) || 0;

            locationCounts.value.set(location, count + 1);
        });

        chartData.value = {
            labels: Array.from(locationCounts.value.keys()),
            datasets: [{
                label: 'Positions',
                data: Array.from(locationCounts.value.values()),
                backgroundColor: '#166534',
            }],
        };
    };

    const loadDashboard = async () => {
        if (isLoading.value) return;

        loadError.value = '';
        isLoading.value = true;

        try {
            const response = await axios.get(
                'https://australia-southeast2-canopy-connect-16c1a.cloudfunctions.net/countPositions'
            );

            const usersSnapshot = await getDocs(collection(db, 'users'));
            const positionsSnapshot = await getDocs(collection(db, 'positions'));

            const counts = {
                viewer: 0,
                editor: 0,
                admin: 0,
            };

            let archivedTotal = 0;

            usersSnapshot.docs.forEach((document) => {
                const role = document.data().role;

                if (userRoles.includes(role)) {
                    counts[role] = counts[role] + 1;
                }
            });

            positionsSnapshot.docs.forEach((document) => {
                if (document.data().archived === true) {
                    archivedTotal = archivedTotal + 1;
                }
            });

            chartPositions.value = positionsSnapshot.docs.map((document) => {
                return document.data();
            });

            updateChart();

            positionCount.value = response.data.count;
            userCount.value = usersSnapshot.size;
            roleCounts.value = counts;
            archivedCount.value = archivedTotal;
        } catch (error) {
            console.error('Loading dashboard failed:', error);
            loadError.value = 'Could not load the dashboard.';
        } finally {
            isLoading.value = false;
        }
    };

    onMounted(() => {
        loadDashboard();
    });
</script>