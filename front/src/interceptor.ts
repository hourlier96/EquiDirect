import axiosInstance from "./helpers/axios"
import { authStore } from "./stores/auth";

const setup = () => {
    axiosInstance.axiosInstance.interceptors.request.use(
    (config) => {
        const token = authStore().accessToken
        if (config.headers) {
            config.headers["Authorization"] = `Bearer ${token}`
            return config;
        }
        
    },
    (error) => {
        return Promise.reject(error);
    }
  );
}

export default setup;