<template>
  <div class="book-view block card">
    <header class="card-header">
      <div class="card-header-title">
        {{ book.title }}
      </div>
    </header>
    <div class="card-content">
      <div class="content">
        {{ book.description }}
      </div>
    </div>
    <div class="card-footer">
      <span v-for="(tag, i) in book.tags" :key="i" class="card-footer-item">{{ tag }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { Book } from "@/types/Book.ts";

export default defineComponent({
  name: "BookView",
  props: {
    book: Object as PropType<Book>,
  },
});
</script>

<style lang="scss">
.book-view {
  width: 50vw;
}
</style>
