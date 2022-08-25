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
    storeUser(userEmail: String, callback: any) {
        const that = this;
        return userAPI.getUserFromEmail(userEmail, (res: any) => {
            if (res[0] !== undefined) {
                that.currentUser = res[0];
                callback();
            }
        });
    },
  },
});
