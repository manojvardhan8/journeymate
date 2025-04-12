document.addEventListener('DOMContentLoaded', function() {
    // Set current year in footer
    const currentYearElement = document.getElementById('current-year');
    if (currentYearElement) {
      currentYearElement.textContent = new Date().getFullYear();
    }
  
    // Mobile menu toggle
    const menuButton = document.querySelector('.mobile-menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    const menuIcon = document.querySelector('.menu-icon');
    
    if (menuButton && mobileMenu && menuIcon) {
      menuButton.addEventListener('click', function() {
        mobileMenu.classList.toggle('hidden');
        menuIcon.textContent = mobileMenu.classList.contains('hidden') ? '☰' : '✕';
      });
    }
  
    // Transport selection
    const transportOptions = document.querySelectorAll('.transport-option');
    const continueButtonContainer = document.querySelector('.continue-button-container');
    const continueButton = document.querySelector('.continue-button');
    const selectedTransportSpan = document.querySelector('.selected-transport');
    let selectedTransport = null;
  
    transportOptions.forEach(option => {
      option.addEventListener('click', function() {
        // Remove selection from all options
        transportOptions.forEach(opt => {
          opt.classList.remove('selected', 'flight', 'train');
        });
  
        // Add selection to clicked option
        selectedTransport = this.getAttribute('data-type');
        this.classList.add('selected', selectedTransport);
        
        // Update continue button
        if (selectedTransportSpan) {
          selectedTransportSpan.textContent = selectedTransport.charAt(0).toUpperCase() + selectedTransport.slice(1);
        }
        
        // Show continue button
        if (continueButtonContainer) {
          continueButtonContainer.classList.remove('hidden');
        }
      });
    });
  
    // Continue button click handler
    if (continueButton) {
      continueButton.addEventListener('click', function() {
        if (selectedTransport) {
          window.location.href = `/selection/?type=${selectedTransport}`;
        }
      });
    }
  
    // Tab switching functionality
    const tabButtons = document.querySelectorAll('.tab-button');
    
    tabButtons.forEach(button => {
      button.addEventListener('click', function() {
        const tabType = this.getAttribute('data-tab');
        
        // Remove active class from all buttons
        tabButtons.forEach(btn => {
          btn.classList.remove('active-flight', 'active-train');
        });
        
        // Add active class to clicked button
        if (tabType === 'flight') {
          this.classList.add('active-flight');
          updateTabContent('flight');
        } else {
          this.classList.add('active-train');
          updateTabContent('train');
        }
      });
    });
  
    function updateTabContent(type) {
      const tabTitle = document.getElementById('tab-title');
      const tabDescription = document.getElementById('tab-description');
      const featureText1 = document.getElementById('feature-text-1');
      const featureIcons = document.querySelectorAll('.feature-item-icon');
      const alertExample = document.getElementById('alert-example');
      const alertType = document.getElementById('alert-type');
      const alertIcon = document.getElementById('alert-icon');
      const alertTitle = document.getElementById('alert-title');
      const routeText = document.getElementById('route-text');
      const oldPrice = document.getElementById('old-price');
      const newPrice = document.getElementById('new-price');
      const seatsRemaining = document.getElementById('seats-remaining');
      const setAlertButton = document.getElementById('set-alert-button');
      
      if (type === 'flight') {
        // Update title and descriptions
        tabTitle.textContent = 'Flight Price Alerts';
        tabTitle.className = 'text-sky-blue';
        tabDescription.textContent = 'Our system monitors flight prices 24/7 and notifies you when prices drop or tickets are running low.';
        featureText1.textContent = 'Get instant alerts when flight prices fall below average';
        
        // Update alert example
        alertExample.className = 'alert-example';
        alertType.className = 'alert-type flight-alert';
        alertIcon.className = 'sky-blue-icon';
        alertTitle.textContent = 'Flight Alert Example';
        routeText.textContent = 'New York → London';
        oldPrice.textContent = '$750';
        newPrice.textContent = '$580';
        seatsRemaining.textContent = '8';
        
        // Update button text
        setAlertButton.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"></path>
            <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"></path>
          </svg>
          Set Flight Alert
        `;
        
        // Update feature icons
        featureIcons.forEach(icon => {
          icon.className = 'feature-item-icon flight-feature-icon';
        });
      } else {
        // Update title and descriptions
        tabTitle.textContent = 'Train Ticket Alerts';
        tabTitle.className = 'text-forest-green';
        tabDescription.textContent = 'Track train ticket availability and get instant notifications when seats are limited or prices change.';
        featureText1.textContent = 'Get instant alerts when train prices fall below average';
        
        // Update alert example
        alertExample.className = 'alert-example train-alert-example';
        alertType.className = 'alert-type train-alert';
        alertIcon.className = 'forest-green-icon';
        alertTitle.textContent = 'Train Alert Example';
        routeText.textContent = 'Paris → Berlin';
        oldPrice.textContent = '$120';
        newPrice.textContent = '$85';
        seatsRemaining.textContent = '12';
        
        // Update button text
        setAlertButton.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"></path>
            <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"></path>
          </svg>
          Set Train Alert
        `;
        
        // Update feature icons
        featureIcons.forEach(icon => {
          icon.className = 'feature-item-icon train-feature-icon';
        });
      }
    }
  });
  document.getElementById('goBtn').onclick = function () {
    const mode = document.getElementById('mode').innerText;

    if (mode === 'Continue with Flight') {
      window.location.href = "{% url 'selection' %}";
    } else if (mode === 'Continue with Train') {
      window.location.href = "{% url 'selection' %}";
    } else {
      alert("Invalid selection");
    }
  };
