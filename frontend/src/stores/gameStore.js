import { defineStore } from "pinia"

export const useGameStore = defineStore("gameStore", {
  state: () => ({
    gameRow: [],
    gameRowBackup: [],
    currentGame: null,
    queuePosition: 0,
  }),
  getters: {
    hasNextGame (state) {
      return state.queuePosition + 1 < state.gameRow.length
    },
    hasPreviousGame (state) {
      return state.queuePosition !== 0
    }
  },
  actions: {
    setGameInRow (newGame) {
        if(!this.gameRow.some(e => e.id === newGame.id)) {
          this.gameRow.push(newGame)
        }
    },
    shuffleRow () {
      this.gameRowBackup = [...this.gameRow]

      this.gameRow.forEach((_, index, array) => {
          const randomIndex =  index + Math.floor(Math.random() * (array.length - index));
          const randomIndexVal = array[randomIndex]
          this.gameRow[randomIndex] = array[index];
          this.gameRow[index] = randomIndexVal;
      })
      this.currentGame = this.gameRow.find(e => e.id === this.currentGame.id)
    },
    unShuffleRow () {
      this.gameRow = this.gameRowBackup
      this.currentGame = this.gameRow.find(e => e.id === this.currentGame.id)
    },
    setCurrentGame (directionValue) {
      this.currentGame  = this.gameRow[this.queuePosition]
      if ((this.queuePosition === 1 && !this.hasNextGame.this.queuePosition) 
      || (this.queuePosition === -1 && !this.hasPreviousGame.this.queuePosition)) {
        return
     }
     this.queuePosition+=directionValue
    },
    clearGameRow () {
      this.gameRow = []
      this.currentGame = null
    }
  },
})



// const hasNextGame = computed(() => {
//   return queuePosition.value + 1 < songs.value.length
// })
// const hasPreviousGame = computed(() => {
//   return queuePosition.value !== 0
// })
