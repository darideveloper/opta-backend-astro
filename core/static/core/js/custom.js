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
  #setupTopmenuLinks() {
    const menuItems = document.querySelectorAll('.d-sm-inline-block a.nav-link')
    menuItems.forEach(item => {

      // Style like a button
      item.classList.add('btn')
      item.classList.add('btn-primary')
      item.classList.add('text-light')

      // Open in new tab
      item.setAttribute('target', '_blank')
    })
  }

  #setupMarkDown() {

    // Get text areas
    const noMarkdownIds = ["description"]
    let textAreasSelector = 'div > textarea'
    textAreasSelector = noMarkdownIds.map(id => `${textAreasSelector}:not(#id_${id})`).join(", ")
    const textAreas = document.querySelectorAll(textAreasSelector)

    setTimeout(() => {
      textAreas.forEach(textArea => {

        new SimpleMDE({
          element: textArea,
          toolbar: [
            "bold", "italic", "heading", "|",
            "quote", "code", "link", "|",
            "unordered-list", "ordered-list", "|",
            "undo", "redo", "|",
            "preview",
          ],
          spellChecker: false,
        })
      })

      // Cahnge code button with uderline
      const codeButton = document.querySelector('a.fa-code')
      if (codeButton) {
        codeButton.classList.remove('fa-code')
        codeButton.classList.add('fa-underline')
        codeButton.setAttribute('title', 'Underline')
        codeButton.setAttribute('data-command', 'underline')
      }
    }, 100)
  }

  /**
   * Disable user permissions and root for no root users
   */
  #disbaleUserPermissionsAndRoot() {

    setTimeout(() => {
      if (!isUserRoot) {

        const userApp = userGroup.split(' ')[0].toLowerCase()

        // Remove superuser and user permissions fields
        const selectors = [
          ".field-is_superuser",
          ".field-user_permissions"
        ]

        selectors.forEach(selector => {
          const element = document.querySelector(selector)
          console.log(selector, element)
          if (element) {
            element.remove()
          }
        })

        // Remove no app permissions
        const groupOptionSelector = ".filtered option"
        const groupOptions = document.querySelectorAll(groupOptionSelector)
        console.log(groupOptions)
        groupOptions.forEach(option => {
          if (!option.title.toLowerCase().includes(userApp)) {
            option.remove()
          }
        })

        // Remove is super use filter
        const superUserFilter = document.querySelector(".changelist-search .form-group:nth-child(2)")
        if (superUserFilter) {
          superUserFilter.remove()
        }

        // Remove user no app group filter
        const groupFilterSelector = 'option[data-name="groups__id__exact"]'
        const groupFilterOptions = document.querySelectorAll(groupFilterSelector)
        groupFilterOptions.forEach(option => {
          if (!option.textContent.toLowerCase().includes(userApp)) {
            option.remove()
          }
        })
      }
    }, 600)

  }

  // /**
  //  * Remove all permissions for the user after save
  //  * This is only for the user edit view
  //  */
  // #removePermissions() {

  //   // Validate we are in the edit view inmediately after save
  //   setTimeout(() => {
  //     const url = window.location.href
  //     const sucessLinkSelector = '.alert-success a'
  //     const sucessLink = document.querySelector(sucessLinkSelector)
  //     const sucessHref = sucessLink?.getAttribute('href')

  //     if (url.includes('change') && url.includes(sucessHref)) {
  //       // Click in remove all permissions btn
  //       const removeBtnSelector = '#id_groups_remove_all_link'
  //       const removeBtn = document.querySelector(removeBtnSelector)
  //       removeBtn.click()
  //     }
  //   }, 300)
  // }

  /**
   * Replace all save buttons with a single continue button
   */
  // #replaceSaveBtnsWidthContinueBtn() {

  //   // Validate if we are in add view
  //   const url = window.location.href
  //   const isAdd = url.includes('add')

  //   if (isAdd) {
  //     // Delete no required buttons
  //     const deleteBtnSelector = 'input[type="submit"]:not([name="_continue"])'
  //     const deleteBtns = document.querySelectorAll(deleteBtnSelector)
  //     deleteBtns.forEach(btn => {
  //       btn.remove()
  //     })

  //     // Update continue button
  //     const saveBtnSelector = 'input[type="submit"]'
  //     const saveBtn = document.querySelector(saveBtnSelector)
  //     saveBtn.value = "Continuar"
  //     saveBtn.innerText = "Continuar"
  //     saveBtn.classList.remove('btn-primary')
  //     saveBtn.classList.add('btn-success')
  //   }
  // }

  /**
   * Run the functions for the current page
   */
  autorun() {

    setTimeout(() => {
      // Global methods
      this.#setupTopmenuLinks()

      // Methods to run for each page
      const methods = {
        "documentos": [() => { this.#setupTagify('[name="palabras_clave"]') }],
        "respuestas": [this.#setupMarkDown],
        "5. respuestas": [this.#setupMarkDown],
        "usuarios": [
          // this.#replaceSaveBtnsWidthContinueBtn,
          // this.#removePermissions,
          this.#disbaleUserPermissionsAndRoot,
        ],
        "entradas": [
          this.#setupMarkDown,
          () => { this.#setupTagify('[name="keywords"]') }
        ],
      }

      // Run the methods for the current page
      if (methods[this.currentPage]) {
        for (let method of methods[this.currentPage]) {
          method.call(this)
        }
      }

    }, 100)

  }
}

new AdminSetup()