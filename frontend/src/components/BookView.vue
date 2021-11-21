<template>
  <div class="book-view">
    {{ book.title }}
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
