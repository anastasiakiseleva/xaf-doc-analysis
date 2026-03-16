---
uid: "113340"
seealso:
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/xaf/archive/2011/05/04/how-to-write-easytests-in-code.aspx
  altText: How to write EasyTests in code
title: 'Custom EasyTest Commands'
owner: Ekaterina Kiseleva
---
# Custom EasyTest Commands

[EasyTest functional testing framework](xref:113211) provides a set of [predefined commands](xref:113208) that cover most of the common use cases. To support specific scenarios, you can implement custom commands. This topic describes the implementation of custom FillDateTimeValue command that is capable of specifying a DateTime value relative to the current date. You can use this command in tests when the application behavior depends on the current date.

## Inherit the Command Class

To implement a custom EasyTest command, inherit the [](xref:DevExpress.EasyTest.Framework.Command) abstract class from the **DevExpress.EasyTest.Framework** namespace. It is recommended that you implement this class in a separate Class Library project of your XAF solution, so it will be built into a separate assembly that can be reused in other XAF applications. Override the **Command.InternalExecute** virtual method and implement the command logics in it. Use the base class' [Command.Parameters](xref:DevExpress.EasyTest.Framework.Command.Parameters) property to access command's parameters. Instantiate the [](xref:DevExpress.EasyTest.Framework.CommandException) class to handle an error. The [ICommandAdapter.CreateTestControl](xref:DevExpress.EasyTest.Framework.ICommandAdapter.CreateTestControl(System.String,System.String)) method exposed by the _adapter_ parameter finds control by its caption and wraps it around an [](xref:DevExpress.EasyTest.Framework.ITestControl) interface. To communicate with the control, use the [ITestControl.GetInterface\<T>](xref:DevExpress.EasyTest.Framework.ITestControl.GetInterface``1) method. The following snippet illustrates the **FillDateTimeValueCommand** command implementation.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Globalization;
using DevExpress.EasyTest.Framework;

namespace AdditionalCommands {
    public class FillDateTimeValueCommand : Command {
        private int GetIntegerParameterValue(string parameterName) {
            int result = 0;
            Parameter parameter = Parameters[parameterName];
            if (parameter != null) {
                if(!Int32.TryParse(parameter.Value, out result)) {
                    throw new CommandException(string.Format(
                        "'{0}' value is incorrect", parameterName), this.StartPosition);
                }
            }
            return result;
        }
        protected override void InternalExecute(ICommandAdapter adapter) {
            int deltaDays = GetIntegerParameterValue("Days");
            int deltaHours = GetIntegerParameterValue("Hours");
            int deltaMinutes = GetIntegerParameterValue("Minutes");
            string cultureName = Parameters["Culture"] != null ? Parameters["Culture"].Value : null;
            CultureInfo currentCulture =
                cultureName != null ? CultureInfo.GetCultureInfo(cultureName) : null;
            string fieldName = Parameters.MainParameter.Value;

            ITestControl testControl = adapter.CreateTestControl(TestControlType.Field, fieldName);
            DateTime dateTime = DateTime.Now.Add(new TimeSpan(deltaDays, deltaHours, deltaMinutes, 0));
            string dateTimeValue = currentCulture != null ? 
                dateTime.ToString(currentCulture) : dateTime.ToString();
            testControl.GetInterface<IControlText>().Text = dateTimeValue;
        }
    }
}
```
***

This command's primary parameter specifies a field caption to be filled. It also takes the Days, Hours, and Minutes extra parameters that specify the differences between the time to be specified and the current time. The Culture extra parameter is intended for overcoming any localization-specific issues.

Note that the [](xref:DevExpress.EasyTest.Framework.IControlText) interface is passed as the **GetInterface\<T>** method's generic parameter. It means that the command's target control provides an editable text. Other supported interfaces are listed in the [](xref:DevExpress.EasyTest.Framework.ITestControl) topic.

## Register the Custom Command
The **WinAdapter** and **WebAdapter** classes are responsible for running the application when testing. In this example we will override the default **WinAdapter** and **WebAdapter** classes. This should be done in separate Class Library projects. These classes are very simple and contain overridden **WinAdapter.RegisterCommands** methods.

**ExtendedWinAdapter Class:**

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.EasyTest.WinAdapter;
using DevExpress.EasyTest.Framework;
using AdditionalCommands;

namespace ExtendedAdapters {
    public class ExtendedWinAdapter : WinAdapter {
        public override void RegisterCommands(IRegisterCommand registrator) {
            base.RegisterCommands(registrator);
            registrator.RegisterCommand("FillDateTimeValue", typeof(FillDateTimeValueCommand));
        }
    }
}
```
***

In the same Class Library project, open the _AssemblyInfo.cs_ (_AssemblyInfo.vb_) file and register the adapter.

# [C#](#tab/tabid-csharp)

```csharp
[assembly: DevExpress.EasyTest.Framework.Adapter(typeof(ExtendedAdapters.ExtendedWinAdapter))]
```
***

**ExtendedWebAdapter Class:**

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.EasyTest.WebAdapter;
using DevExpress.EasyTest.Framework;
using AdditionalCommands;

namespace ExtendedAdapters {
    public class ExtendedWebAdapter : WebAdapter {
        public override void RegisterCommands(IRegisterCommand registrator) {
            base.RegisterCommands(registrator);
            registrator.RegisterCommand("FillDateTimeValue", typeof(FillDateTimeValueCommand));
            ScriptParser scriptParser = ((ScriptParser)registrator);
        }
    }
}
```
***

In the same Class Library project, open the _AssemblyInfo.cs_ (_AssemblyInfo.vb_) file and register the adapter.

# [C#](#tab/tabid-csharp)

```csharp
[assembly: DevExpress.EasyTest.Framework.Adapter(typeof(ExtendedAdapters.ExtendedWebAdapter))]
```
***

The resulting solution structure is illustrated in the image below (new and modified files are highlighted).

![CustomEasyTestCommand_SolutionStructure](~/images/customeasytestcommand_solutionstructure116893.png)

## Configure EasyTest to use Custom Adapter Classes
In order to use custom Adapter assemblies instead of default ones, the [EasyTest configuration file](xref:113209) must be modified in the following manner.

# [XML](#tab/tabid-xml)

```XML
<Options>
    <!-- ... -->
    <Aliases>
        <Alias Name="WinAdapterFileName" 
        Value="[SolutionPath]\ExtendedWinAdapter\bin\Debug\ExtendedWinAdapter.dll" />
        <Alias Name="WebAdapterFileName" 
        Value="[SolutionPath]\ExtendedWebAdapter\bin\Debug\ExtendedWebAdapter.dll" />
    <!-- ... -->
  </Aliases>
</Options>
```

***

## A Sample Script that Uses the FillDateTimeValue Command
To see the **FillDateTimeValue** command in action, add the **Event** class from the [Business Class Library](xref:112571). Then, create and run the following EasyTest script.

# [ETS](#tab/tabid-ets)

```ETS
#DropDB AdditionalCommands
#Application AdditionalCommandsWin
#Application AdditionalCommandsWeb
 
*Action Navigation(Scheduler Event)
 
*Action New
 
*FillDateTimeValue Start Date/Time
 Culture = en-US
 Days = -1
 Hours = 1
*FillDateTimeValue End Date/Time
 Culture = en-US
 
*Action Save
```
***

## Debug Custom Command
Use the following approach when you need to debug a custom EasyTest command implementation

* Set the Class Library project that contains the FillDateTimeValue command implementation as StartUp.
* Set required breakpoints in the command's code.
* Open project properties and modify the **Start external program** and **Command line arguments** options under the **Debug** tab. The first should point to the [TestExecutor](xref:113210) utility, the latter - to the script that uses the command.
	
	![CustomEasyTestCommand_Debug](~/images/customeasytestcommand_debug116894.png)

Now you can set breakpoints in a command's code and debug.
