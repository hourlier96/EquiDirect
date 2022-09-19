import api from "@/helpers/axios";

export default {
  name: "users",
  async getUserFromEmail(email) {
    return await api.get(this.name, email);
  },
  async createUser(firstName, lastName, email, password, role) {
    return await api.post(this.name, {
      firstname: firstName,
      lastname: lastName,
      email: email,
      password: password,
      role: role,
    });
  },
};
