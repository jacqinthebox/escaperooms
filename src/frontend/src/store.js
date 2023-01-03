import { writable } from 'svelte/store';

export const redirect = writable(null);
export const teamStore = writable({
    teamName: '',
    email: '',
    score: 0,
    });