<template>
  <div class="books-view">
    <BookView v-for="(book, i) in getBooks()" :key="i" :book="book"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Book } from "@/types/Book.ts";
import BookView from "@/components/BookView.vue";

export default defineComponent({
  name: "BooksView",

  components: {
    BookView,
  },

  methods: {
    getBooks(): Book[] {
      return [
        {
          title: "Livre 1",
          description: "Ceci est un livre (un)",
          tags: ["livre", "un"],
        },
        {
          title: "Livre 2",
          description: "Ceci est un livre (deux)",
          tags: ["livre", "deux"],
        },
      ];
    },
  },
});
</script>
