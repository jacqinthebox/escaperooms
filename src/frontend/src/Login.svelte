<script>
    import Cookies from 'js-cookie';
    //import {set} from 'svelte/store';
    //import {teamStore} from './store.js';
    const apiUrl = process.env.API_URL;

    let email = '';
    let password = '';
    let errorMessage = '';
    let teamName = '';

    async function handleSubmit(event) {
        event.preventDefault();

        try {
            const response = await fetch(process.env.API_URL + '/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    password: password,
                    email: email
                })
            });

            const data = await response.json();
            console.log("posted request");
            console.log(apiUrl)
            if (response.status !== 200) {
                errorMessage = "Wrong password or username (or this login function fails miserably)" + response.url;
            } else {
                Cookies.set('email', email, {expires: 3600});
                teamName = data.teamName;
                Cookies.set('teamName', teamName, {expires: 3600});
                window.location = '/';
            }
        } catch (error) {
            console.error(error);
            errorMessage = 'An unknown error has occurred. This is so bad.';
        }
    }
</script>


<section class="section">
    <div class="container">
        <h1 class="title">Login</h1>
        {#if errorMessage}
            <div class="notification is-danger">
                <p>{errorMessage}</p>
            </div>
        {/if}
        <form on:submit|preventDefault={handleSubmit}>
            <div class="field">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">Email</label>
                <div class="control">
                    <input class="input" type="text" name="email" bind:value={email} required>
                </div>
            </div>
            <div class="field">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">Password</label>
                <div class="control">
                    <input class="input" type="password" name="password" bind:value={password} required>
                </div>
            </div>
            <div class="field">
                <div class="control">
                    <button class="button is-link" type="submit">Submit</button>
                </div>
            </div>
        </form>
    </div>
</section>
