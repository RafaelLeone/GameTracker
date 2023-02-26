import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
    getGames: () => {
      return new Promise((resolve, reject) => {
        api
          .get("/api/games/list_games")
          .then((response) => {
            return resolve(response.data)
          })
          .catch((error) => {
            return reject(error)
          })
      })
    },
    addNewgame: (data) => {
      return new Promise((resolve, reject) => {
        api
          .post("/api/games/add_game", apiHelpers.dataToForm(data))
          .then((response) => {
            return resolve(response.data)
          })
          .catch((error) => {
            return reject(error)
          })
      })
    },
    deleteGame: (data) => {
      return new Promise((resolve, reject) => {
        api
          .post("/api/games/delete_game", apiHelpers.dataToForm(data))
          .then((response) => {
            return resolve(response.data)
          })
          .catch((error) => {
            return reject(error)
          })
      })
    },
    changeStatus: (data) => {
      return new Promise((resolve, reject) => {
        api
          .post("/api/games/change_status", apiHelpers.dataToForm(data))
          .then((response) => {
            return resolve(response.data)
          })
          .catch((error) => {
            return reject(error)
          })
      })
    },
  }
  