import { defineStore } from "pinia";
import { storage } from "@/helpers/storage";

import individualAPI from "@/api/resources/individual";

export const individualStore = defineStore({
  id: "individual",
  state: () => ({
    id: null,
    user_id: null,
  }),
  getters: {
    id: (state) => state.id,
    userId: (state) => state.user_id,
  },
  actions: {
  }
});
