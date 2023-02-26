<template>
   <div>
      <h5 class="text-h5 text-left font-weight-bold ml-5">Your games</h5>
      <div class="label">
        <div class="bg-red text-right mgn rounded">
          <span>I want to play</span>
        </div>
        <div class="bg-yellow text-right mgn rounded">
          <span>I'm playing</span>
        </div>
        <div class="bg-green text-right mgn rounded">
          <span>Schmoved it :)</span>
        </div>
      </div>
      <v-spacer></v-spacer>
    <v-row class="mt-10 mgn">
      <v-card v-for="game in apiGames.games" :key="game.title" rounded class="shadow-on-hover ma-2" :class="getClass(game)" @click="selectedGame(game)">
        <v-img :src="game.cover" height="145" width="145" class="mx-4 mt-4"></v-img>
        <v-card-title>{{ reduceTitle(game.title) }}</v-card-title>
        <v-card-subtitle class="mb-6">{{ game.platform }}</v-card-subtitle>
        <v-btn @click="deleteGame(game)">DELETE</v-btn>
      </v-card>
    </v-row>
    <div class="text-right mgn">
      <span>Click to change ;)</span>
    </div>
  </div>
</template>

<script>
import { useGameStore } from "@/stores/gameStore"
import { ref, onMounted } from 'vue'
import gamesApi from "@/api/games.api.js"


const apiGames = ref([]) 

export default {
  setup () {
    const gameStore = useGameStore()
    const rating = ref(0)

    async function getAPIGames () {
      apiGames.value = await gamesApi.getGames()
    }

    onMounted(async () => {
      await getAPIGames()
    })

    return { gameStore, apiGames, rating }
  },
  methods: {
    async deleteGame(newGame) {
      await gamesApi.deleteGame({id: newGame.id})
      apiGames.value = await gamesApi.getGames()
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
    async selectedGame(newGame) {
      if (newGame.status == 3) {
        newGame.status = 1
      } else {
        newGame.status += 1
      }
      await gamesApi.changeStatus({id: newGame.id, new_status: newGame.status})
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
.label {
  display: flex;
}
.mgn {
  margin-left: 2%;
  margin-top: 2%;
  padding: 1%;
}
</style>