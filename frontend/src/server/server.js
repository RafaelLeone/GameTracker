import { createServer, Model, Factory } from "miragejs"
import { faker } from '@faker-js/faker';

export function makeServer({ environment = "development" } = {}) {
  let server = createServer({
    environment,
    
    models: {
      game: Model,
    },

    factories: {
      game: Factory.extend({
        title() {
          return faker.game.gameName()
        },
        platform () {
          return faker.name.fullName()
        },
        cover () {
          return faker.image.cats(145, 145, true)
        },
        file () {
          return "src/assets/shakira.mp3"
        }
      })
    },

    seeds(server) {
      server.createList("game", 10)
    },

    routes() {
      this.urlPrefix = 'http://localhost';
      this.namespace = "api"
      this.get("games/list_games", schema => {
        return schema.games.all()
      })

    },
  })

  return server
}