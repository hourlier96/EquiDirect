import api from "@/helpers/axios";

export default {
  name: "auth",
  async getJwt(email, password) {
    return await api.post(`${this.name}/token`, email, password);
  },

  async createUser(firstName, lastName, email, password, role) {
    return await api.post(`${this.name}/register`, {
      firstname: firstName,
      lastname: lastName,
      email: email,
      password: password,
      role: role,
    });
  },
};
