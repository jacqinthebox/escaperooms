<script>
    let email = '';
    let password = '';
    let errorMessage = '';
  
    async function handleSubmit(event) {
      event.preventDefault();
  
      try {
        const response = await fetch('http://localhost:5001/login', {
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
        if (response.status !== 200) {
          errorMessage = data.error;
        } else {
          // Redirect to the dashboard or show a success message
        }
      } catch (error) {
        console.error(error);
        errorMessage = 'An error occurred';
      }
    }
  </script>

    <section class="section">
        <div class="container">
        <h1 class="title">Login</h1>
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
