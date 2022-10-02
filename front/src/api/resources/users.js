import api from "@/helpers/axios";

export default {
  name: "users",
  async getUserFromEmail(payload) {
    if (payload.access_token) {
      return await api.get(
        this.name,
        { email: payload.email, multiple: false },
        {
          Authorization: `Bearer ${payload.access_token}`,
        }
      );
    }
    return await api.get(this.name, { email: payload.email, multiple: false });
  },
  // Called when validating email link
  async getUserFromEmailAndConfirmId(payload) {
    return await api.get(
      this.name,
      {
        email: payload.email,
        confirmation_id: payload.confirmation_id,
        multiple: false,
      },
      {
        Authorization: `Bearer ${payload.access_token}`,
      }
    );
  },
  async confirmUser(id, payload, access_token) {
    return await api.put(this.name, id, payload, {
      Authorization: `Bearer ${access_token}`,
    });
  },
};
