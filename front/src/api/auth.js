import api from "@/helpers/axios";

export default {
  name: "auth",
  async getJwt(email, password) {
    return await api.post(`${this.name}/token`, email, password);
  },
};
