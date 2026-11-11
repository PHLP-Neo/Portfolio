import { ref } from 'vue'
import { collection, getDocs } from 'firebase/firestore';
import { db } from './firebase/init.js';

export const positions = ref([]);

export const loadPositions = async () => {
    const snapshot = await getDocs(collection(db, 'positions'));

    const loadedPositions = snapshot.docs.map((document) => {
        return {
            id: document.id,
            title: document.data().title,
            location: document.data().location,
            description: document.data().description,
            ratings: [],
            selectedRating: '',
            archived: document.data().archived === true,
        };
    });

    for (const position of loadedPositions) {
        const ratingsSnapshot = await getDocs(
            collection(db, 'positions', position.id, 'ratings')
        );

        position.ratings = ratingsSnapshot.docs.map((document) => {
            return {
                userId: document.id,
                score: document.data().score,
            };
        });
    }

    positions.value = loadedPositions;
};