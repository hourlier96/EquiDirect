import axios from "axios";
import { APISettings } from "@/api/config"

const axiosInstance = axios.create(APISettings);

export default {
    axiosInstance,
    async get(entity, params) {
        return await axiosInstance(
            {
                method: "GET",
                url: `/${entity}/`,
                params: params
            }
        )
    },
    async post(entity, payload) {
        return await axiosInstance(
            {
                method: "POST",
                url: `/${entity}/`,
                data: payload
            }
        )
    },
    async put(entity, payload) {
        return await axiosInstance(
            {
                method: "PUT",
                url: `/${entity}/`,
                data: payload
            }
        )
    },
    async delete(entity, id) {
        return await axiosInstance(
            {
                method: "DELETE",
                url: `/${entity}/${id}`,
            }
        )
    }
}