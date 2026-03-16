---
uid: DevExpress.ExpressApp.XafApplication.CustomizeLanguagesList
name: CustomizeLanguagesList
type: Event
summary: Occurs when setting up the application.
syntax:
  content: public event EventHandler<CustomizeLanguagesListEventArgs> CustomizeLanguagesList
seealso: []
---
When localizing your application, you should list all the languages supported by your application in the configuration file (see [Localize Standard XAF Modules and DevExpress Controls Used in an Application](xref:113301)). If you need to customize this list while starting the application, subscribe to the **CustomizeLanguagesList** event. Get the list of the languages specified in the application's configuration file using the event handler's _CustomizeLanguagesListEventArgs.Languages_ parameter.

> [!NOTE]
> In the Windows Forms solution template, the WinApplication class' descendant handles this event, to add the language of the current UI culture.