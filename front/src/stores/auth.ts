import { defineStore } from "pinia";
import authAPI from "@/api/auth";

const defaultUser = {
  id: null,
  email: null,
  firstname: null,
  lastname: null,
  role: null,
  confirmation_id: null,
  confirmed: null,
  created_at: null
};

export const authStore = defineStore({
  id: "auth",
  state: () => ({
    currentUser: { ...defaultUser },
    accessToken: null,
  }),
  getters: {
    userEmail: (state) => state.currentUser.email,
    userName: (state) =>
      state.currentUser.firstname + " " + state.currentUser.lastname,
    userRole: (state) => state.currentUser.role,
  },
  actions: {
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
  persist: true,
});
