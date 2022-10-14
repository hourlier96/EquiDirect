import api from "@/helpers/axios";

export default {
  name: "individual",
  async getIndividualFromUser(payload) {
    return await api.get(this.name, {
      user_id: payload.user_id,
      multiple: false,
    });
  },
};
