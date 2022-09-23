import { defineStore } from "pinia";

import userAPI from "@/api/resources/users"
import authAPI from "@/api/auth"

export const authStore = defineStore({
  id: "auth",
  state: () => ({
    currentUser: {
        email: null,
        firstname: null,
        lastname: null,
        role: null
    },
    accessToken: null
  }),
  getters: {
    userEmail: (state) => state.currentUser.email,
    userName: (state) => state.currentUser.firstname + " " + state.currentUser.lastname,
    userRole: (state) => state.currentUser.role
  },
  actions: {
    async getJwt(userEmail: String, password: String) {
      const response = await authAPI.getJwt(userEmail, password)
      this.accessToken = response.data.access_token
    },

    async storeUser(userEmail: String) {
        const response = await userAPI.getUserFromEmail(userEmail)
        this.currentUser = response.data;
    },
    async signIn(firstName: String, lastName: String, userEmail: String, password: String, role: String) {
      const response = await userAPI.createUser(firstName, lastName, userEmail, password, role)
      this.currentUser = response.data[0]
    }
  }
});
