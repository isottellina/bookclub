<template>
  <div class="main-container">
    <BooksView />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import BooksView from "@/components/BooksView.vue";

export default defineComponent({
  name: "Home",

  components: {
    BooksView,
  },
});
</script>

<style lang="scss">
.main-container {
  display: flex;
  flex-direction: column;

  align-items: center;
}
</style>
