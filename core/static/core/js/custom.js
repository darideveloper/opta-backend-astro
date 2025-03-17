class AdminSetup {

  /**
 * Setup global data
 */
  constructor() {
    // Get current page
    this.currentPage = document.querySelector('.content h1').textContent.toLowerCase().trim()
    console.log(this.currentPage)

    // Run methods in each page
    this.autorun()
  }

  #showAlert() {
    alert("Custom JS Working")
  }

  #setupTagify(inputSelector) {
    const input = document.querySelector(inputSelector)
    if (input) {
      const tagify = new Tagify(input, {
        whitelist: [],
        dropdown: {
          classname: "color-blue",
          enabled: 0,
          maxItems: 5
        }
      })
    }
  }

  /**
   * Run the functions for the current page
   */
  autorun() {
    // Methods to run for each page
    const methods = {
      "modificar documento": [this.#setupTagify('[name="palabras_clave"]')],
      "añadir documento": [this.#setupTagify('[name="palabras_clave"]')],
    }

    // Run the methods for the current page
    if (methods[this.currentPage]) {
      for (let method of methods[this.currentPage]) {
        method.call(this)
      }
    }
  }
}

new AdminSetup()