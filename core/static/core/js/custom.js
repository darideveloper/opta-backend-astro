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

  /**
   * Setup Tagify for the given input selector
   * @param {string} inputSelector - The selector for the input element
   */
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
   * Setup the style for the top menu links
   */
  #setupTopmenuLinksStyle() {
    const menuItems = document.querySelectorAll('.d-sm-inline-block a.nav-link')
    menuItems.forEach(item => {
      item.classList.add('btn')
      item.classList.add('btn-primary')
      item.classList.add('text-light')
    })
  }

  /**
   * Run the functions for the current page
   */
  autorun() {

    // Global methods
    this.#setupTopmenuLinksStyle()

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