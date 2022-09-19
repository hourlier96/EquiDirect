import api from "@/helpers/axios";

export default {
  name: "users",
  async getUserFromEmail(email) {
    return await api.get(this.name, email);
  },
};
