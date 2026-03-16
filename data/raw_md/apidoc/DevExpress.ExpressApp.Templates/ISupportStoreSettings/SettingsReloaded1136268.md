---
uid: DevExpress.ExpressApp.Templates.ISupportStoreSettings.SettingsReloaded
name: SettingsReloaded
type: Event
summary: Occurs when Template settings are reloaded.
syntax:
  content: event EventHandler SettingsReloaded
seealso:
- linkId: "117231"
---
Implement this event in Templates that support the ISupportStoreSettings interface. This event can be used to customize the window - change  template control settings after default settings were applied (e.g., from the Application Model). For instance, you can control the form size, location, toolbar visibility, etc.