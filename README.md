# Relay

> Nothing is out of reach.

Relay is an iOS/iPadOS accessibility app that reads any physical 
touchscreen — ATM, self-checkout, vending machine, restaurant kiosk — 
using the device camera. It reconstructs the interface accessibly on 
the user's screen and enables full interaction without physically 
touching the kiosk.

Built by a full-time power wheelchair user who knows firsthand what 
it means to face a screen you cannot reach.

---

## The problem

Millions of people cannot physically reach or interact with touchscreen kiosks. These interfaces are not designed for wheelchair users, people with motor disabilities, the elderly, or people of short stature. Relay gives anyone the ability to interact with any kiosk fully independently — from their own device.

---

## How it works

**Phase 1 — Screen reader (active)**
Camera reads the kiosk screen using computer vision and OCR. Relay 
reconstructs an accessible version of the interface on the user's 
device. The user taps elements on their phone and then Relay guides them precisely.

**Phase 2 — Audio control (planned)**
Relay utilizes the kiosk's ADA-required headphone jack. User taps 
on reconstructed UI — audio signal controls the kiosk. No touching 
required.

**Phase 3 — Bluetooth HID (planned)**
Relay sends a Bluetooth HID signal. User taps on reconstructed UI — 
kiosk responds wirelessly. Full independence. Zero contact.

---

## Tech stack

**Learning environment (Mac)**
- Python 3.14, OpenCV, PyTorch, Tesseract OCR, NumPy

**Ship target (iPhone/iPad)**
- Swift, SwiftUI, AVFoundation, Vision framework, CoreML, CoreBluetooth

---

## Status

- [x] Dev environment set up
- [x] Live camera feed working
- [ ] OCR pipeline
- [ ] UI element detection
- [ ] Interface reconstruction
- [ ] CoreML conversion
- [ ] iOS app
- [ ] App Store submission

---

## Built by

Eric Pineda — CS Student, Fresno State  
NSF USHER Scholar | AIIS Lab Researcher | Apple AIML Engineering Track