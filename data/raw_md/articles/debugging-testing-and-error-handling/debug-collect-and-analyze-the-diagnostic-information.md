---
uid: "117344"
seealso:
- linkId: "403656"
- linkId: "402148"
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/k18568/how-to-enable-script-debugging
  altText: How to enable script debugging
- linkId: "112818"
- linkId: "113484"
title: Debug, Collect and Analyze the Diagnostic Information
owner: Ekaterina Kiseleva
---
# Debug, Collect and Analyze the Diagnostic Information

XAF applications support collecting diagnostic information using common approaches applicable to any .NET applications. This topic lists Visual Studio settings required to collect error information and describes how to analyze this information.

## Server-Side Exceptions

### Adjust Visual Studio Settings

Before debugging an error, modify the following Visual Studio settings:

* Click **Tools** | **Options…** to invoke the **Options** dialog. In the left-hand panel, choose the **Debugging** | **General** category and disable the [Just My Code](https://learn.microsoft.com/en-us/visualstudio/debugger/just-my-code) option.
	
	![Debug_JustMyCode](~/images/debug_justmycode125313.png)
* Enable **Common Language Runtime Exceptions** in the **Exception Settings** window. If this window is hidden, click **Debug** | **Windows** | **Exception Settings** in Visual Studio's menu (see [Managing Exceptions with the Debugger](https://learn.microsoft.com/en-us/visualstudio/debugger/managing-exceptions-with-the-debugger)).
	
	![Debug_ClrExceptions2015](~/images/debug_clrexceptions2015125315.png)

### Analyze the Diagnostic Information
You can now run your application and reproduce the error. Open the [Call Stack](https://learn.microsoft.com/en-us/visualstudio/debugger/how-to-use-the-call-stack-window) window and view the routines that are currently in the stack.

* If the routines at the top of the call stack refer to third-party libraries, you can search for the error message and call stack text in public community resources like [Stack Overflow](https://stackoverflow.com/), where possible solutions may already be discussed.
* If there are DevExpress routines at the top of the call stack, [contact the DevExpress support team](https://supportcenter.devexpress.com/). Attach your project, the [eXpressAppFramework.log](xref:112575) file, the full exception call stack and inner exceptions info to the support ticket. If the error relates to your database content, attach a backup of the database as well.

## Client-Side Exceptions

You can use the Developer Tools to trace client-side errors and get more information about them. Refer to the following help topic for more details: [Diagnose Client-Side Errors](xref:404015#diagnose-client-side-errors).

## Debugging

* [First look at the Visual Studio Debugger](https://learn.microsoft.com/en-us/visualstudio/debugger/debugger-feature-tour)
* [Debug Managed Code (C#, F#, C++/CLI)](https://learn.microsoft.com/en-us/visualstudio/debugger/debugging-managed-code)
* [Debugging User Interface Reference](https://learn.microsoft.com/en-us/visualstudio/debugger/debugging-user-interface-reference)
* [Manage exceptions with the debugger in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/managing-exceptions-with-the-debugger)
* [How can I debug DevExpress .NET source code using PDB files](xref:403656)
* [How to enable script debugging](https://supportcenter.devexpress.com/ticket/details/k18568/how-to-enable-script-debugging)
