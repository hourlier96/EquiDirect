import api from "@/helpers/axios";

export default {
  name: "email",
  async sendVerificationMail(emails, confirmation_id) {
    return await api.post(`${this.name}`, { email: emails, confirmation_id });
  },
};
