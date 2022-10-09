import { defineStore } from "pinia";

import { storage } from "@/helpers/storage";
import authAPI from "@/api/auth";

const defaultUser = {
  id: null,
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
      id: storage.getAuth().currentUser.id || null,
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
    async storeUser(user) {
      this.currentUser = user;
      console.log("Logged user: ", user);
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
