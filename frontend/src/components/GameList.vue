<template>
   <div >
    <v-row>
      <h5 class="text-h5 font-weight-bold ml-5">Your games</h5>
      <v-spacer></v-spacer>

    </v-row>
    <v-row class="mt-10">
      <v-card v-for="game in apiGames.songs" :key="game.title" rounded class="shadow-on-hover ma-2" :class="getClass(game)" @click="gameChoosed(game)">
        <v-img :src="game.cover" height="145" width="145" class="mx-4 mt-4"></v-img>
        <v-card-title>{{ reduceTitle(game.title) }}</v-card-title>
        <v-card-subtitle class="mb-6">{{ game.platform }}</v-card-subtitle>
        <v-btn @click="deleteGame(game)">DELETE</v-btn>
      </v-card>
    </v-row>

    <!-- <v-row class="mt-12">
      <v-col class="pa-0">
        <h5 class="text-h5 font-weight-bold mb-1">Rate your games</h5>
      </v-col>
      <v-spacer></v-spacer>
      <span class="caption grey--text mr-2">SEE ALL</span>
    </v-row>
    <v-row class="mt-12">
      <v-card
        v-for="game in apiGames.songs"
        :key="game.title"
        min-width="360"
        class="mr-5"
      >
        <div class="d-flex justify-between">
          <v-card-title class="flex-grow-1 flex-column align-start">
            <div class="text-h5">
              {{ game.title }}
            </div>
            <div class="text-h6 font-weight-thin">{{ game.platform }}</div>
          </v-card-title>
          <v-img
            contain
            height="125px"
            :src="game.cover"
            style="flex-basis: 125px"
            class="flex-grow-0"
          ></v-img>
        </div>

        <v-divider></v-divider>

        <v-card-actions class="pa-4">
          Rate this game
          <v-spacer></v-spacer>
          <span class="text-grey text-caption me-2">
            ({{ rating }})
          </span>

          <v-rating
            v-model="rating"
            color="green"
            active-color="green"
            half-increments
            hover
            size="18"
          ></v-rating>
        </v-card-actions>
      </v-card>
    </v-row> -->
  </div>
</template>

<script>
import { useGameStore } from "@/stores/gameStore"
import { ref, onMounted } from 'vue'
import songsApi from "@/api/songs.api.js"


const apiGames = ref([]) 

export default {
  setup () {
    const gameStore = useGameStore()
    const rating = ref(0)

    async function getAPIGames () {
      apiGames.value = await songsApi.getGames()
    }

    onMounted(async () => {
      await getAPIGames()
    })

    return { gameStore, apiGames, rating }
  },
  methods: {
    async deleteGame(newGame) {
      await songsApi.deleteGame({id: newGame.id})
      apiGames.value = await songsApi.getGames()
    },
    getClass(newGame) {
      if (newGame.status == 1) {
        return 'red'
      }
      if (newGame.status == 2) {
        return 'yellow'
      }
      if (newGame.status == 3) {
        return 'green'
      }
    },
    gameChoosed(newGame) {
      if (newGame.status == 3) {
        newGame.status = 1
      } else {
        newGame.status += 1
      }
    },
    reduceTitle (title) {
      if (title.length <= 15) {
        return title
      }
      return title.slice(0,13)+'...'
    }
  },
}
</script>

<style>
.shadow-on-hover:hover {
  background-color: purple;
  box-shadow: 0 10px 15px -3px purple,
    0 4px 6px -2px darkpurple;
}
.red {
  background-color: red;
  box-shadow: 0 10px 15px -3px red,
    0 4px 6px -2px darkred;
}
.yellow {
  background-color: yellow;
  box-shadow: 0 10px 15px -3px yellow,
    0 4px 6px -2px yellow;
}
.green {
  background-color: green;
  box-shadow: 0 10px 15px -3px green,
    0 4px 6px -2px darkgreen;
}
</style>