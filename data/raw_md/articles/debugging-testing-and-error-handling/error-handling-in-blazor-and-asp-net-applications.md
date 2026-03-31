---
uid: "112704"
seealso: []
title: Error Handling in ASP.NET Core Blazor
---
# Error Handling in ASP.NET Core Blazor

This topic demonstrates error handling mechanisms used in ASP.NET Core Blazor applications and explains how to customize them.

XAF ASP.NET Core Blazor applications support error handling out of the box.

XAF displays toast notifications for errors that implement `IUserFriendlyException`. The following image shows an example with validation error messages:

![|XAF ASP.NET Core Blazor Toast Message, DevExpress](~/images/xaf-blazor-error-handling-toast-message-devexpress.png)

XAF displays a pop-up window in debug mode with detailed error information for errors that occur in Views and their toolbars (for example, when XAF cannot render a View):

![|XAF ASP.NET Core Blazor Pop-up Window, DevExpress](~/images/xaf-blazor-error-handling-popup-window-devexpress.png)

For security, the pop-up window does not contain the stack trace in production mode.

When such errors occur, we recommend that you click **Refresh Page** to refresh the browser window and load a new application instance that does not contain incorrect data. In this case, you lose unsaved changes.

To save your changes before you reload the application, click **Cancel** or **Close** to hide the pop-up window. Copy unsaved data. We do not recommend that you continue working with a corrupted application state. Reload the app to avoid additional errors.

Click **Copy Details** to copy the error message for debugging.

In case of a critical error, XAF displays a full-screen error page. For example, the following page may appear on application startup if XAF has written incorrect data to the database:

![|XAF ASP.NET Core Blazor Pop-up Window, DevExpress](~/images/xaf-blazor-error-handling-full-screen-error-devexpress.png)
