<template>
    <section class="mb-4" aria-label="Volunteer opportunity map">
        <h2 class="h5">Opportunity Locations</h2>

        <p class="small" role="status">
            Map received {{ props.matchingPositions.length }} matching position(s).
        </p>

        <button
            type="button"
            class="btn btn-success mb-3"
            :disabled="isLoadingPins || isRouting
                || props.matchingPositions.length === 0 || mapError !== ''"
            @click="showMatchingJobs"
        >
            {{ isLoadingPins ? 'Loading locations…' : 'Show Matching Jobs' }}
        </button>

        <div v-if="pinsError" class="alert alert-danger" role="alert">
            {{ pinsError }}
        </div>

        <p class="small">
            Green pins show matching jobs at their listed suburb.
            Click a pin to see the job titles.
        </p>

        <form
            v-if="positionLocations.length > 0"
            class="mb-3"
            @submit.prevent="findNearestJobs"
        >
            <label for="nearest-origin" class="form-label">
                Your starting suburb or address
            </label>

            <input
                id="nearest-origin"
                v-model="nearestOriginQuery"
                type="text"
                class="form-control mb-2"
                :disabled="isFindingNearest"
                required
            >

            <button
                type="submit"
                class="btn btn-outline-success"
                :disabled="isFindingNearest || isLoadingPins || isRouting"
            >
                {{ isFindingNearest ? 'Finding…' : 'Find Three Nearest Jobs' }}
            </button>
        </form>

        <div v-if="nearestError" class="alert alert-danger" role="alert">
            {{ nearestError }}
        </div>

        <div v-if="nearestJobs.length > 0" class="mb-3">
            <h3 class="h5">Nearest matching jobs</h3>

            <p>Starting location: {{ nearestFrom }}</p>
            <p class="small">
                Approximate straight-line distances to the listed suburbs.
            </p>

            <ol>
                <li
                    v-for="entry in nearestJobs"
                    :key="entry.position.id"
                    class="mb-2"
                >
                    <strong>{{ entry.position.title }}</strong>
                    — {{ entry.position.location }}
                    — {{ entry.distanceKm.toFixed(1) }} km
                    <button
                        type="button"
                        class="btn btn-outline-primary btn-sm ms-2"
                        :disabled="isRouting || isLoadingPins || isFindingNearest"
                        @click="showJobRoute(entry)"
                    >
                        Show Walking Route
                    </button>
                </li>
            </ol>
        </div>

        <div v-if="mapError" class="alert alert-danger" role="alert">
            {{ mapError }}
        </div>

        <div v-if="routeError" class="alert alert-danger" role="alert">
            {{ routeError }}
        </div>

        <div v-if="routeDetails" class="alert alert-info" role="status">
            <p>From: {{ routeDetails.from }}</p>
            <p>To: {{ routeDetails.to }}</p>
            <p class="mb-0">
                Walking distance: {{ routeDetails.kilometres }} km.
                Estimated time: {{ routeDetails.minutes }} minutes.
            </p>
        </div>

        <div ref="mapContainer" class="opportunity-map"></div>

    </section>
</template>

<script setup>
    import { ref, onMounted, onBeforeUnmount, watch } from 'vue'; 
    //onBeforeUnmount: cleans up when leaving the component.
    import mapboxgl from 'mapbox-gl'; //Mapbox’s map, marker and drawing tools.
    import 'mapbox-gl/dist/mapbox-gl.css';
    import axios from 'axios';

    const mapError = ref(''); //log error
    const destinationLabel = ref(''); //selected job title and suburb
    const destinationCoordinates = ref(null); //pos of job for routing
    const originQuery = ref(''); //starting address
    const isRouting = ref(false); //whether a walking route is requested
    const routeError = ref(''); //calc drawing fails
    const routeDetails = ref(null); //details
    const isLoadingPins = ref(false); // task busy loading pins
    const pinsError = ref(''); //failure loading pins
    const positionLocations = ref([]); //one entry per job contains job obj and coordinante
    const nearestOriginQuery = ref(''); //start location text in textbox
    const nearestJobs = ref([]); // up to three
    const nearestFrom = ref(''); //starting position
    const nearestError = ref(''); //job search fails
    const isFindingNearest = ref(false); // if running nearest calc.

    const props = defineProps({
        matchingPositions: { // Jobs received from PositionsView
            type: Array,
            default: () => [],
        },
    });

    const mapContainer = ref(null); //actual html element <div>

    let originMarker = null; //orange start marker
    let destinationMarker = null; //blue destination marker
    let map = null; //map instance
    let jobMarkers = []; //array of green pins

    onMounted(() => {
        const token = import.meta.env.VITE_MAPBOX_TOKEN;

        if (!token) {
            mapError.value = 'Map configuration is missing.';
            return;
        }

        try {
            mapboxgl.accessToken = token;

            map = new mapboxgl.Map({
                container: mapContainer.value, //html element it appears
                style: 'mapbox://styles/mapbox/streets-v12', //street style
                center: [144.9631, -37.8136], //initial location
                zoom: 10, //init zoom
            });

            map.addControl(new mapboxgl.NavigationControl());

            map.on('error', (event) => {
                console.error('Map loading failed:', event.error);
                mapError.value = 'The map could not load completely.';
            });
        } catch (error) {
            console.error('Map setup failed:', error);
            mapError.value = 'Could not display the map.';
        }
    });

    const geocodeLocation = async (query) => {
        const response = await axios.get(
            'https://api.mapbox.com/search/geocode/v6/forward',
            {
                params: {
                    q: query,
                    country: 'au',
                    proximity: '144.9631,-37.8136',
                    autocomplete: false,
                    limit: 1,
                    access_token: import.meta.env.VITE_MAPBOX_TOKEN,
                },
            }
        );

        if (response.data.features.length === 0) {
            throw new Error('No matching location found.');
        }

        return response.data.features[0];
    };

    const showMatchingJobs = async () => {
        if (!map || isLoadingPins.value || isRouting.value) {
            return;
        }

        clearMatchingPins();
        pinsError.value = '';

        const matchingJobs = props.matchingPositions;

        if (matchingJobs.length === 0) return;

        isLoadingPins.value = true;

        try {
            const groups = new Map();

            matchingJobs.forEach((position) => {
                const key = position.location.trim().toLowerCase();

                if (!groups.has(key)) {
                    groups.set(key, {
                        location: position.location,
                        jobs: [],
                    });
                }

                groups.get(key).jobs.push(position);
            });

            const locations = [];

            for (const group of groups.values()) {
                const result = await geocodeLocation(
                    group.location + ', Victoria, Australia'
                );

                if (!map || props.matchingPositions !== matchingJobs) return;

                locations.push({
                    jobs: group.jobs,
                    coordinates: result.geometry.coordinates,
                    address: result.properties.full_address,
                });
            }

            const bounds = new mapboxgl.LngLatBounds();

            locations.forEach((location) => {
                const titles = location.jobs.map((job) => {
                    return job.title;
                }).join(' • ');

                const popup = new mapboxgl.Popup({ offset: 25 })
                    .setText(location.address + ' — ' + titles);

                const marker = new mapboxgl.Marker({ color: '#166534' })
                    .setLngLat(location.coordinates)
                    .setPopup(popup)
                    .addTo(map);

                jobMarkers.push(marker);
                bounds.extend(location.coordinates);

                location.jobs.forEach((job) => {
                    positionLocations.value.push({
                        position: job,
                        coordinates: location.coordinates,
                    });
                });
            });

            map.fitBounds(bounds, { padding: 50, maxZoom: 13 });
        } catch (error) {
            console.error('Loading job pins failed:', error);
            clearMatchingPins();
            pinsError.value = 'Could not display matching jobs on the map.';
        } finally {
            isLoadingPins.value = false;
        }
    };

    const clearMatchingPins = () => {
        jobMarkers.forEach((marker) => {
            marker.remove();
        });

        jobMarkers = [];
        positionLocations.value = [];
        nearestJobs.value = [];
        nearestFrom.value = '';
        nearestError.value = '';
    };

    const findNearestJobs = async () => {
        if (isFindingNearest.value || isLoadingPins.value || isRouting.value) return;

        nearestJobs.value = [];
        nearestFrom.value = '';
        nearestError.value = '';
        clearSelectedRoute();

        if (!nearestOriginQuery.value.trim()) {
            nearestError.value = 'Enter your starting address.';
            return;
        }

        if (positionLocations.value.length === 0) {
            nearestError.value = 'Show matching jobs on the map first.';
            return;
        }

        const locations = positionLocations.value;
        isFindingNearest.value = true;

        try {
            const origin = await geocodeLocation(
                nearestOriginQuery.value.trim()
            );

            if (positionLocations.value !== locations) return;

            const start = mapboxgl.LngLat.convert(
                origin.geometry.coordinates
            ); // convert to Mapbox object for distance calculation

            const rankedJobs = locations.map((entry) => {
                const destination = mapboxgl.LngLat.convert(
                    entry.coordinates
                );

                return {
                    position: entry.position,
                    coordinates: entry.coordinates,
                    distanceKm: start.distanceTo(destination) / 1000,
                };
            });

            rankedJobs.sort((first, second) => {
                return first.distanceKm - second.distanceKm;
            });

            nearestJobs.value = rankedJobs.slice(0, 3);
            nearestFrom.value = origin.properties.full_address;
        } catch (error) {
            console.error('Finding nearest jobs failed:', error);
            nearestError.value = 'Could not find the nearest jobs.';
        } finally {
            isFindingNearest.value = false;
        }
    };

    const clearSelectedRoute = () => {
        clearRoute();

        if (destinationMarker) {
            destinationMarker.remove(); //remove destination marker
            destinationMarker = null;
        }

        destinationCoordinates.value = null;
        destinationLabel.value = '';
        routeDetails.value = null;
        routeError.value = '';
    };

    onBeforeUnmount(() => {
        clearMatchingPins();

        if (map) {
            map.remove();
            map = null;
        }
    });

    watch(() => props.matchingPositions, () => { //tells vue to watch the incoming marching job array, triggered when filteredPosition was replaced
        clearMatchingPins();
        clearSelectedRoute();
        pinsError.value = '';
    });

    const clearRoute = () => {
        if (originMarker) {
            originMarker.remove(); //remove starting marker
            originMarker = null;
        }

        if (!map) return;

        if (map.getLayer('walking-route')) {
            map.removeLayer('walking-route');
        }

        if (map.getSource('walking-route')) {
            map.removeSource('walking-route');
        }
    };

    const showJobRoute = async (entry) => {
        if (!map || isRouting.value || isLoadingPins.value || isFindingNearest.value) return;

        destinationCoordinates.value = entry.coordinates;

        destinationLabel.value =
            entry.position.title + ' — ' + entry.position.location;

        originQuery.value = nearestFrom.value;

        if (destinationMarker) {
            destinationMarker.remove();
        }

        destinationMarker = new mapboxgl.Marker({ color: '#0ea5e9' })
            .setLngLat(entry.coordinates)
            .setPopup(
                new mapboxgl.Popup({ offset: 25 })
                    .setText(destinationLabel.value)
            )
            .addTo(map);

        await getWalkingRoute();
    };

    const getWalkingRoute = async () => {
        if (isRouting.value) return;

        clearRoute();

        routeError.value = '';
        routeDetails.value = null;

        if (!destinationCoordinates.value || !originQuery.value.trim()) {
            routeError.value = 'Find a destination and enter your starting address.';
            return;
        }

        const destination = destinationCoordinates.value;
        const destinationName = destinationLabel.value;
        const locations = positionLocations.value;
        isRouting.value = true;

        try {
            const origin = await geocodeLocation(originQuery.value.trim());
            const start = origin.geometry.coordinates;

            const response = await axios.get(
                'https://api.mapbox.com/directions/v5/mapbox/walking/' +
                start.join(',') + ';' + destination.join(','),
                //start = [144.9, -37.8];
                //destination = [145.1, -37.9];
                //144.9,-37.8;145.1,-37.9
                {
                    params: {
                        geometries: 'geojson', //we can use this format for drawing
                        overview: 'full', //request the full route
                        access_token: import.meta.env.VITE_MAPBOX_TOKEN,
                    },
                }
            );

            if (!map || positionLocations.value !== locations) return; //if map removed or job location changed

            if (!response.data.routes || response.data.routes.length === 0) {
                routeError.value = 'No walking route found.';
                return;
            } //need 1+ route return

            const route = response.data.routes[0];

            drawRoute(route.geometry);

            originMarker = new mapboxgl.Marker({ color: '#c2410c' })
                .setLngLat(start)
                .addTo(map);

            routeDetails.value = {
                from: origin.properties.full_address,
                to: destinationName,
                kilometres: (route.distance / 1000).toFixed(1),
                minutes: Math.ceil(route.duration / 60),
            };
        } catch (error) {
            console.error('Getting walking route failed:', error);
            routeError.value = 'Could not calculate the walking route.';
        } finally {
            isRouting.value = false;
        }
    };

    const drawRoute = (geometry) => {
        if (!map || !map.isStyleLoaded()) {
            throw new Error('The map is still loading.');
        }

        map.addSource('walking-route', { //add a data source
            type: 'geojson',
            data: {
                type: 'Feature',
                properties: {}, //no need for extra descriptive attributes
                geometry: geometry,
            },
        });

        map.addLayer({
            id: 'walking-route', //use the source walking-route
            type: 'line',
            source: 'walking-route',
            layout: {
                'line-join': 'round', //cornet and end are round
                'line-cap': 'round',
            },
            paint: {
                'line-color': '#166534', //green
                'line-width': 5,
            },
        });

        const bounds = new mapboxgl.LngLatBounds();

        geometry.coordinates.forEach((coordinate) => {
            bounds.extend(coordinate);
        });

        map.fitBounds(bounds, { padding: 50 });
    };

</script>

<style scoped>
    .opportunity-map {
        width: 100%;
        height: 420px;
    }
</style>