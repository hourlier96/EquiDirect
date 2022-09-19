import axios from "axios";
import { APISettings } from "@/api/config"

export default {
    async get(entity, params) {
        return await axios(
            {
                method: "GET",
                url: `${APISettings.baseURL}/${entity}/`,
                params: params
            }
        )
    },
    async post(entity, payload) {
        return await axios(
            {
                method: "POST",
                url: `${APISettings.baseURL}/${entity}/`,
                data: payload
            }
        )
    },
    async put(entity, payload) {
        return await axios(
            {
                method: "PUT",
                url: `${APISettings.baseURL}/${entity}/`,
                data: payload
            }
        )
    },
    async delete(entity, id) {
        return await axios(
            {
                method: "DELETE",
                url: `${APISettings.baseURL}/${entity}/${id}`,
            }
        )
    }
}