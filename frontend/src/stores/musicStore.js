import { defineStore } from "pinia"

export const useMusicStore = defineStore("musicStore", {
  state: () => ({
    musicRow: [],
    musicRowBackup: [],
    currentGame: null,
    queuePosition: 0,
  }),
  getters: {
    hasNextGame (state) {
      return state.queuePosition + 1 < state.musicRow.length
    },
    hasPreviousGame (state) {
      return state.queuePosition !== 0
    }
  },
  actions: {
    setMusicInRow (newMusic) {
        if(!this.musicRow.some(e => e.id === newMusic.id)) {
          this.musicRow.push(newMusic)
        }
    },
    shuffleRow () {
      this.musicRowBackup = [...this.musicRow]

      this.musicRow.forEach((_, index, array) => {
          const randomIndex =  index + Math.floor(Math.random() * (array.length - index));
          const randomIndexVal = array[randomIndex]
          this.musicRow[randomIndex] = array[index];
          this.musicRow[index] = randomIndexVal;
      })
      this.currentGame = this.musicRow.find(e => e.id === this.currentGame.id)
    },
    unShuffleRow () {
      this.musicRow = this.musicRowBackup
      this.currentGame = this.musicRow.find(e => e.id === this.currentGame.id)
    },
    setCurrentGame (directionValue) {
      this.currentGame  = this.musicRow[this.queuePosition]
      if ((this.queuePosition === 1 && !this.hasNextGame.this.queuePosition) 
      || (this.queuePosition === -1 && !this.hasPreviousGame.this.queuePosition)) {
        return
     }
     this.queuePosition+=directionValue
    },
    clearMusicRow () {
      this.musicRow = []
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
