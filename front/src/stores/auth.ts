import { defineStore } from "pinia";

import { storage } from "@/helpers/storage";
import userAPI from "@/api/resources/users";
import authAPI from "@/api/auth";

const defaultUser = {
  email: null,
  firstname: null,
  lastname: null,
  role: null,
  confirmation_id: null,
  confirmed: null,
};

export const authStore = defineStore({
  id: "auth",
  state: () => ({
    currentUser: {
      email: storage.getAuth().currentUser.email || null,
      firstname: storage.getAuth().currentUser.firstname || null,
      lastname: storage.getAuth().currentUser.lastname || null,
      role: storage.getAuth().currentUser.role || null,
      confirmation_id: storage.getAuth().currentUser.confirmation_id || null,
      confirmed: storage.getAuth().currentUser.confirmed || null,
    },
    accessToken: storage.getAuth().accessToken || null,
  }),
  getters: {
    userEmail: (state) => state.currentUser.email,
    userName: (state) =>
      state.currentUser.firstname + " " + state.currentUser.lastname,
    userRole: (state) => state.currentUser.role,
  },
  actions: {
    resetUser() {
      this.currentUser = defaultUser;
      this.accessToken = null;
    },
    async getJwt(userEmail: String, password: String) {
      return await authAPI.getJwt(userEmail, password);
    },
    async storeUser(userEmail: String) {
      const response = await userAPI.getUserFromEmail(userEmail);
      console.log(response);
      this.currentUser = response.data;
    },
    async signIn(
      firstName: String,
      lastName: String,
      userEmail: String,
      password: String,
      role: String
    ) {
      const response = await authAPI.createUser(
        firstName,
        lastName,
        userEmail,
        password,
        role
      );
      return response;
    },
  },
});

export default defaultUser;
