<script>
  import Cookies from 'js-cookie';
  Cookies.remove('email', {});
  Cookies.remove('teamName', {});

  function redirect() {
    const intervalId = window.setInterval(() => {
      window.location = '/';
      window.clearInterval(intervalId);
    }, 5000);
  }

  redirect()
</script>


<section class="section">
  <div class="container">
    <h1 class="title">Bye!</h1>
      <p>You have been logged out! If you want, you can
        <a href="/">login</a> again. You will be redirected shortly.</p>

  </div>
</section>