import { defineStore } from "pinia";

import userAPI from "@/api/resources/users"

export const authStore = defineStore({
  id: "auth",
  state: () => ({
    currentUser: {
        email: null,
        firstname: null,
        lastname: null,
        role: null
    },
  }),
  getters: {
    userEmail: (state) => state.currentUser.email,
    userName: (state) => state.currentUser.firstname + " " + state.currentUser.lastname,
    userRole: (state) => state.currentUser.role
  },
  actions: {
    async storeUser(userEmail: String) {
        const that = this;
        const response = await userAPI.getUserFromEmail(userEmail)
        that.currentUser = response.data[0]
    },
    async signIn(firstName: String, lastName: String, userEmail: String, password: String, role: String) {
      const that = this;
      const response = await userAPI.createUser(firstName, lastName, userEmail, password, role)
      that.currentUser = response.data[0]
    }
  }
});
