<template>
  <nav class="navbar is-danger">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">Bookclub</router-link>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Navbar",
});
</script>
