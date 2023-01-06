<script>
    import Success from "./Success.svelte";
    import {onMount} from "svelte";

    let apiUrl = '';

    onMount(() => {
        apiUrl = `${window.location.protocol}//${window.location.host}`;
        const hostParts = window.location.host.split(':');
        const host = hostParts[0];

        if (host === '127.0.0.1' || host === '0.0.0.0' || host === 'localhost') {
            apiUrl = `${window.location.protocol}//${host}:5000`;
        }
    });

    let team_name = '';
    let contact_name = '';
    let email = '';
    let password = '';
    let errorMessage = '';
    let registered = false;
    export const emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    //export const spacesRegex = /^\S*$/;

    function validateEmail(email) {
        if (!emailRegex.test(email)) {
            errorMessage = 'Invalid email address';
        } else {
            errorMessage = '';
        }
    }

    /*
    function validateTeam(team_name) {
        if (!spacesRegex.test(team_name)) {
            errorMessage = 'No spaces are allowed in the Teamname because it is too complicated to escape them :(.';
        } else {
            errorMessage = '';
        }
    } */

    async function handleSubmit(event) {
        event.preventDefault();

        try {
            const response = await fetch(apiUrl + '/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    TeamName: team_name,
                    ContactName: contact_name,
                    Password: password,
                    Email: email
                })
            });

            const data = await response.json();
            if (response.status !== 200) {
                errorMessage = data.message;
                console.log(data)
            } else {
                console.log(data)
                registered = true;
            }
        } catch (error) {
            console.error(error);
            errorMessage = 'An unknown error has occurred';
        }
    }
</script>

{ #if registered }
    <Success/>
{:else}


    <section class="section">
        <div class="container">
            <h1 class="title">Registration</h1>

            {#if errorMessage}
                <div class="notification is-danger">
                    <p>{errorMessage}</p>
                </div>
            {/if}

            <form on:submit|preventDefault={handleSubmit}>
                <div class="field">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="label">What will be group name? Be sure to make it a funny one.</label>
                    <div class="control">
                        <input class="input" type="text" name="team_name" bind:value={team_name} required>
                    </div>
                </div>
                <div class="field">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="label">What is your name?</label>
                    <div class="control">
                        <input class="input" type="text" name="contact_name" bind:value={contact_name} required>
                    </div>
                </div>
                <div class="field">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="label">What is your email address?</label>
                    <div class="control">
                        <input class="input" type="text" name="email" bind:value={email}
                               on:input={event => validateEmail(event.target.value)} required>
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
{/if}