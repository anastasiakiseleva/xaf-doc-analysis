---
uid: "113208"
seealso:
- linkId: "113211"
- linkId: "113293"
- linkId: "113345"
- linkId: "113294"
title: EasyTest Script Reference
---
# EasyTest Script Reference

The script language provided by EasyTest is used to define the testing actions that must be performed by a test script. The language allows you to perform various operations over an XAF application's UI, using very simple syntax. This topic describes that script language syntax and provides a list of all the available test commands. For general information on how to create test scripts and run them, refer to the [EasyTest Basics](xref:113211) topic. To see how to extend EasyTest command set, refer to the [How to: Implement a Custom EasyTest Command](xref:113340) topic.

## EasyTest Script Syntax

EasyTest script files are translated line-by-line. A line that does not have a white space at the beginning is considered to have a command in it. If a line has a starting white space, the line is expected to have a parameter for the preceding command on this line. There can also be as many blank lines as necessary. 

To comment out a command, start a line with the semicolon character.

# [ETS](#tab/tabid-ets)

```ETS
; This is a comment. The next line contains a commented out command.
; *Action Contacts
```

***


Generally, a command is a multi-line structure that has the following syntax:

``prefix command-name [primary-parameter [(primary-parameter-argument)] ]``

``[ SPACE secondary-parameter-name[[index]] operator value1 [, value2 [, value3 ...]]]``

``[ SPACE secondary-parameter-name[[index]] operator value1 [, value2 [, value3 ...]]]``

``...``

{|
|-

! Element
! Description
|-

| _prefix_
| Specifies the command type. The following prefixes are available.

* **#** - the following command is a pre-processor directive. Most of these commands do not take part in test flow and can be located anywhere within the file. They are only used to configure tests.
* **&#0042;** - the following command should be successfully executed. If the command does not succeed, this is considered an error, and test execution will be interrupted.
* **!** - the following command's execution should fail. If it does not fail, the test script considers this as error, and test execution stops.

Note that each command does not necessarily support all the prefixes.
|-

| _command-name_
| The name of the command to be executed. For the complete command list, see below.
|-

| _primary-parameter_
| Many commands require a single parameter. In this instance, the primary parameter should be used.
|-

| _primary-parameter-argument_
| Primary parameters sometimes require additional information. For instance, if a command is to execute an Action and the primary parameter is the Action name, you may also need to specify an argument for the specified Action; e.g., if an Action locates a record by ID, you need to specify the ID.
|-

| _secondary-parameter-name_,

 _value1_,

 _value2_,

 ...
| If multiple parameters are required for a command, their name and value pairs are specified on individual lines after the command statement.   These pairs can be either assignment or comparison statements. A parameter name must be prefixed by a single white space to indicate that it is a parameter and not the next command. Some parameters can take a list of values, separated by a comma. If a value contains comma symbols, enclose this value in quotes to avoid interpreting this value as a list.
|-

| _operator_
| The following operators are allowed by EasyTest syntax.

* **=** - serves as an assignment or comparison operator.
* **!=** - comparison operator. Specifies that a parameter should not be equal to a specified value.
|}

You can use [wildcards and regular expressions](#wildcards-and-regular-expressions) in parameter values.

The following table list commands that can be used in EasyTest scripts.

{|
|-

! [Preprocessor Directives](#preprocessor-directives)
! [Common Commands](#common-commands)
! [Table Commands](#table-commands)
! [File Operation Commands](#file-operation-commands)
|-

| [Application](#application)

[DropDB](#dropdb)

[IncludeFile](#includefile)

[IfDef](#ifdef)

[EndIf](#endif)

[RestoreDB](#restoredb)

[Timeout](#timeout)
| [Action](#action)

[ActionAvailable](#actionavailable)

[ActionVisible](#actionvisible)

[CheckActionsHint](#checkactionshint)

[CheckActionValue](#checkactionvalue)

[CheckFieldValues](#checkfieldvalues)

[CheckValidationResult](#checkvalidationresult)

[CompareScreenshot](#comparescreenshot)

[ExecuteEditorAction](#executeeditoraction)

[FieldVisible](#fieldvisible)

[FillForm](#fillform)

[HandleDialog](#handledialog)

[OptionalAction](#optionalaction)

[ReopenApplication](#reopenapplication)

[SetActiveWindowSize](#setactivewindowsize)

[SetStringCompareMode](#setstringcomparemode)

[Sleep](#sleep)
| [CheckTable](#checktable)

[CheckTableSelection](#checktableselection)

[ClearSelection](#clearselection)

[ExecuteColumnEditorAction](#executecolumneditoraction)

[ExecuteTableAction](#executetableaction)

[FillRecord](#fillrecord)

[ProcessRecord](#processrecord)

[SelectRecords](#selectrecords)

[UnselectRecords](#unselectrecords)
| [CheckFileExists](#checkfileexists)

[CompareFiles](#comparefiles)

[CopyFile](#copyfile)

[DeleteFile](#deletefile)
|}

Command descriptions and examples are provided below.

## Preprocessor Directives
Preprocessor directives begin with the hash sign. These commands do not define any actions; use them to obtain information about the application being tested, database to be used, timeouts, etc. Certain preprocessor directives take an application name or a database name as a parameter. These names must be defined in the [EasyTest configuration file](xref:113209).

***

### Application

Prefix: "#", Parameters: Primary.

This is a required command - a test script should contain at least one [Application](#application) command. The primary parameter specifies the name of the application to be tested.

# [ETS](#tab/tabid-ets)

```ETS
#Application MyAppWin
```

***

***

### DropDB

Prefix: "#", Parameters: Primary.

Deletes the database specified by the main parameter. This command can potentially destroy a lot of valuable data and should be used with caution.

# [ETS](#tab/tabid-ets)

```ETS
#DropDB TestDB
```

***

***

### IncludeFile

Prefix: "#", Parameters: Primary.

Allows you to include a set of commands from an external file into the current script. Instructs the preprocessor to treat the contents of the specified file as if those contents had appeared in the current script at the point where the command is located. You cannot include a standalone test script with the IncludeFile command, as the [Application](#application) command will be duplicated in the result script.

# [ETS](#tab/tabid-ets)

```ETS
#IncludeFile LogonProcedure.inc
```

***

***

### IfDef

Prefix: "#", Parameters: Primary.

Allows you to control test flow, depending on which application is currently being tested. The primary parameter specifies an application. Commands between this pre-processor directive and the corresponding [EndIf](#endif) directive are executed only for the specified application. Nested **IfDef** sections are not supported.

# [ETS](#tab/tabid-ets)

```ETS
#IfDef MyAppWin
```

***

***

### EndIf

Prefix: "#", Parameters: None.

Concludes an [IfDef](#ifdef) section.

# [ETS](#tab/tabid-ets)

```ETS
#EndIf
```

***

***

### RestoreDB

Prefix: "#", Parameters: Primary.

Restores the database specified by the main parameter from a backup. The database name must be defined in the configuration file with an additional specified **BackupFileName** parameter.

# [ETS](#tab/tabid-ets)

```ETS
#RestoreDB TestDB
```

***

***

### Timeout

Prefix: "#", Parameters: Primary.

Specifies the testing time limit. The primary parameter specifies the overall testing time in minutes. Use this command if you believe that the default test time limit specified in the [EasyTest configuration file](xref:113209) will be exceeded.

# [ETS](#tab/tabid-ets)

```ETS
#Timeout 20
```

***

***

## Common Commands
Common commands allow you to perform a wide variety of operations. Usually, these commands can be used in any View. In certain scenarios you may need to use fully qualified names.

* To refer to an Action located within a nested frame in a command that takes an Action name as a parameter, use the following syntax: _nested-frame-caption_._Action-caption_ (for example, **Children.New**).
* To refer to a Property Editor located within a nested frame represented by the [DetailPropertyEditor](xref:113572) in a command that takes a field name as a parameter, use the following syntax: _nested-frame-caption_._Field-caption_ (for example, **Manager.First Name**).

***

### Action

Prefix: "*" and "!", Parameters: Primary (with argument).

Executes an Action or activates a tab with a nested View. When the **Action** command is used to execute an Action, the primary parameter specifies the Action caption. The primary parameter's argument specifies data for the Action. When the **Action** command is used to activate a tab, the primary parameter specifies the tab's caption.

# [ETS](#tab/tabid-ets)

```ETS
*Action Navigation(Contacts)

*Action Children.New

*Action Contacts
```
***

To select a nested menu item, use the following syntax:

# [ETS](#tab/tabid-ets)

```ETS
*Action Set Task(Priority.Low)
```
***

![|easy test action select nested item](~/images/easy-test-action-select-nested-item.png)

***

### ActionAvailable

Prefix: "*" and "!",  Parameters: Primary.

Checks to see if the Action specified by the primary parameter is visible and enabled.

# [ETS](#tab/tabid-ets)

```ETS
!ActionAvailable Children.New
```

***

***

### ActionVisible

Prefix: "*" and "!", Parameters: Secondary.

Checks to see if the Action specified by the primary parameter is visible.

# [ETS](#tab/tabid-ets)

```ETS
*ActionVisible Save
```

***

***

### CheckActionsHint

Prefix: "*",  Parameters: Secondary.

Checks a hint text in specified Actions. This is useful if you need to check disabled Actions for a disability reason, since these reasons are included in Action hints.

**Note**: to check multi-line hints, use multiple secondary parameters with indexer notation. Also note that you do not need to check all lines within a multi-line hint.

# [ETS](#tab/tabid-ets)

```ETS
*CheckActionsHint 
 Delete[0] = Delete
 Delete[1] = Requires selection
```

***

***

### CheckActionValue

Prefix: "*" and "!",  Parameters: Secondary.

Checks the current value of a Single Choice or Parametrized Action.

# [ETS](#tab/tabid-ets)

```ETS
*CheckActionValue View(Default)
```

***

***

### CheckFieldValues

Prefix: "*",  Parameters: Secondary.

Requires an active Detail View (or a WinForms form). Checks whether field values conform to conditions specified by secondary parameters. To check multi-line text values, use multiple secondary parameters with indexer notation. Also note that you do not need to check all lines within a multi-line text. In a regular WinForms form, you can access field values by the editor controls' names (or captions or tags).

# [ETS](#tab/tabid-ets)

```ETS
*CheckFieldValues
 Name = Nick
 Age != 20

*CheckFieldValues
 ErrorInfo[0] = Data Validation Error:*
 ErrorInfo[1] = - "Name" must contain "Word1". 
 ErrorInfo[2] = - "Name" must contain "Word2".
```

***

***

### CheckValidationResult

Prefix: "*" and "!", Parameters: Secondary.

Checks currently displayed Validation results. Supports display of validation results (pop-up window) in Windows Forms. The following secondary parameters can be specified.

* **Message** - optional. Checks the primary validation error message.
* **Columns** - optional. Considered for Windows Forms applications. It specifies captions of the **DisplayableValidationResultItem** List View columns to be tested. You can specify two Target and Description column captions, or a single 'Description' column. If the **Columns** parameter is omitted, a column with the "Description" caption is tested.
* **Info** - optional. Checks validation results (rule target and description) of each broken rule. When testing against a single "Description" column is specified via the **Columns** parameter, then the Info parameter value is the description text (for example, _"Title" must not be empty._). When testing against "Target" and "Description" is specified, then the Info parameter value is the validation target name and the description text, separated by a comma (for example, _Mary Tellitson, "Age" must be greater than or equal to "18"._ ).
* **SkipUnexpectedErrors**  - optional. When set to True, disables the checking of validation errors not specified by **Info** parameters. The default value is False, so the [CheckValidationResult](#checkvalidationresult) command execution fails when there are unexpected validation errors.

More details on the [CheckValidationResult](#checkvalidationresult) command are provided in the [How to: Test Validation Rules](xref:113294) topic.

# [ETS](#tab/tabid-ets)

```ETS
*CheckValidationResult
 Message = Data Validation Error: *
 Info = "Title" must not be empty.

*CheckValidationResult
 Columns = Target, Description
 Message = Data Validation Error: *
 Info = Mary Tellitson, "Age" must be greater than or equal to "18".
 SkipUnexpectedErrors = True
```

***

***

### CompareScreenshot

Prefix: "*" and "!",  Parameters: Primary and secondary.

Takes the screenshot of the active window (or browser's content) and compares it with the template PNG image specified by the primary parameter. When the script is executed for the first time and there are no templates, the test execution fails and this command creates a template image located in the _Images_ subfolder of the configuration file folder. The actual testing is performed on subsequent test runs, and the command fails if the current and template screenshots are not identical. It is recommended to use the [CompareScreenshot](#comparescreenshot) command together with the [SetActiveWindowSize](#setactivewindowsize) command to guarantee that window sizes on the current and template screenshots are the same. The **Mask** secondary parameter can be used to exclude certain screenshot areas from comparison. A mask is a duotone PNG file.

# [ETS](#tab/tabid-ets)

```ETS
*CompareScreenshot MySolution01.png
```

***

***

### ExecuteEditorAction

Prefix: "*" and "!", Parameters: Primary (with argument).

Executes an Action supplied by a Lookup Property Editor or an Object Property Editor. The command's primary parameter specifies the name of the Property Editor. The primary parameter's argument specifies a Lookup Property Editor's Action.

# [ETS](#tab/tabid-ets)

```ETS
*ExecuteEditorAction Manager

*ExecuteEditorAction Issue(Clear)

*ExecuteEditorAction File

*ExecuteEditorAction File(Browse)
```

***

***

### FieldVisible

Prefix: "*" and "!", Parameters: Secondary.

Checks whether the Property Editor specified by the primary parameter is visible.

# [ETS](#tab/tabid-ets)

```ETS
!FieldVisible User
```

***

***

### FillForm

Prefix: "*" and "!", Parameters: Secondary.

Requires an active Detail View. Fills fields with values. Secondary parameters specify field captions (or control names, or control tags in WinForms) and their values. Lookup fields are supported as well.

# [ETS](#tab/tabid-ets)

```ETS
*FillForm
 First Name = Jill
 Last Name = Green
 Department = Sales Department
```

***

***

### HandleDialog

Prefix: "*" and "!", Parameters: Secondary.

Handles dialog windows in Windows Forms applications. This command can have secondary parameters.

* **Caption** - optional. Checks the window caption.
* **Message** - optional. Checks the dialog's message text. If the specified and actual messages match, the command responds to the dialog as specified by the first parameter. Otherwise, the test fails.
* **Respond** - optional. Specifies the desired response. This parameter's value is a dialog button's caption (Yes/OK or No/Cancel).

To check multi-line messages, use multiple Message parameters with indexer notation. An example of using this command is provided in the [How to: Test Validation Rules](xref:113294) topic.

# [ETS](#tab/tabid-ets)

```ETS
*HandleDialog
 Caption = FormCaption
 Message[0] = Line1
 Message[1] = Line2
 Respond = Yes
```

***

> [!NOTE]
> EasyTest is not designed to manage language-specific messages in a language-independent way. Use a language-specific string for the **Caption** and **Respond** parameters in accordance with the current language settings.

***

### OptionalAction

Prefix: "*", Parameters: Primary (with argument).

Acts like the [Action](#action) command. The difference is that this command does not require the target Action to be visible and active. If the Action is hidden or inactive, this command does nothing. The [OptionalAction](#optionalaction) command can be useful when creating platform-independent scripts.

# [ETS](#tab/tabid-ets)

```ETS
*OptionalAction Edit
```

***

***

### ReopenApplication

Prefix: "*", Parameters: Primary.

Closes the application being tested and reopens it. This command can be useful when you need to check whether some changes are persisted between application runs. The optional primary parameter specifies the name of application to be opened after closing the current one.

# [ETS](#tab/tabid-ets)

```ETS
*ReopenApplication

*ReopenApplication MySolutionWeb
```

***

> [!NOTE]
> In WinForms applications, this command executes the **Exit** Action where a name can be different in other languages. In this case, the **Exit** Action cannot be found and the test will fail.

***

### SetActiveWindowSize

Prefix: "*", Parameters: Primary.

Resizes an active window. Use this command before the [CompareScreenshot](#comparescreenshot) command to guarantee that window sizes on the current and template screenshots are the same. The primary parameter specifies the new window size in a '**Width**x**Height**' format.

# [ETS](#tab/tabid-ets)

```ETS
*SetActiveWindowSize 640x480
```

***

***

### SetStringCompareMode

Prefix: "*", Parameters: Primary.

Changes the string comparison mode for commands that follow this command. Supported modes, specified using the primary parameter,  are **Wildcards** (default) and **Regex**. For details, see the [Wildcards and Regular Expressions](#wildcards-and-regular-expressions) section below.

# [ETS](#tab/tabid-ets)

```ETS
*SetStringCompareMode Regex

*SetStringCompareMode Wildcards
```

***

***

### Sleep

Prefix: "*", Parameters: Primary.

Suspends the test execution for a specified time. The primary parameter specifies the delay in milliseconds. Generally, you do not need to use this command.

# [ETS](#tab/tabid-ets)

```ETS
*Sleep 500
```

***

***

## Table Commands
Table commands perform various operations over List Editors. A table command's primary parameter is optional; it specifies the frame caption where the target List View is located. For example, you can use this parameter when you need to check a Detail View's nested List View.

***

### CheckTable

Prefix: "*", Parameters: Primary and secondary.

Checks whether field values in specified records match values specified by secondary parameters. The following secondary parameters should be specified.

* **Columns** - optional. Lists fields where values are to be compared to parameter values.
* **Row**- optional. This parameter specifies the values to look for in specified fields. Note that there can be more than one **Row** parameter, if you wish to test multiple records simultaneously. You can pass "*" to this parameter to test the first available row. To test a row with a specific number, use a zero-based index (e.g Row[5] = _value_).
* **CheckInvisibleColumns** - optional. Specifies whether hidden columns are checked or not. Considered in Windows Forms applications only.
* **RowCount** - optional. Specifies how many rows are expected in a table. Both the "!=" and "=" operators are supported.

When no secondary parameters are specified, the command checks that a table is empty.

# [ETS](#tab/tabid-ets)

```ETS
*CheckTable Contacts
 Columns = ID, Name
 Row[0] = 1, Sam
 Row = 5, Nataly
 Row = 6, Dan
 CheckInvisibleColumns = True
```

***

***

### CheckTableSelection

Prefix: "*", Parameters: Primary and secondary.

Checks to see if the currently selected records match values specified by secondary parameters. The following secondary parameters should be specified.

* **Columns** - required. Lists the selected records' fields where values are to be compared to parameter values.
* **Row** - required. This parameter specifies the values to look for in the specified fields. Note that there can be more than one **Row** parameter, if you wish to test multiple selected records simultaneously.  You can pass "*" to this parameter to test the first available row. To test a row with a specific number, use a zero-based index (e.g Row[5] = _value_).

# [ETS](#tab/tabid-ets)

```ETS
*CheckTableSelection Contacts
 Columns = First Name
 Row = Mary
```

***

***

### ClearSelection

Prefix: "*", Parameters: Primary and secondary.

Clears the selection in a List View.

# [ETS](#tab/tabid-ets)

```ETS
*ClearSelection Tasks
```

***

***

### ExecuteColumnEditorAction

Prefix: "*" and "!", Parameters: Primary and secondary.

Executes an Action supplied by an in-place Lookup Property Editor or an in-place Object Property Editor. The following secondary parameters should be specified.

* **Column** - required. Specifies the required column represented by an in-place Lookup Property Editor or an in-place Object Property Editor.
* **Action** - required. Specifies a Lookup Property Editor's Action. Should be an empty value for Object Property Editors.

# [ETS](#tab/tabid-ets)

```ETS
*ExecuteColumnEditorAction Phones
 Column = Type
 Action = Find

*ExecuteColumnEditorAction
 Column = Address
 Action = ''
```

***

***

### ExecuteTableAction

Prefix: "*" and "!", Parameters: Primary and secondary.

Performs a custom action supported by a particular List Editor.

The `DevExpress.ExpressApp.Scheduler.Blazor.SchedulerBlazorModule` and [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) support the following actions:

* **CheckVisibleResources** - checks the visible resources.
* **CheckSelectedEventResources** - checks to see if the selected event is associated with the specific resources.
* **CheckAppointmentType** - checks to see if the focused appointment has a specific type. Possible appointment types include Normal, Occurrence and ChangedOccurrence.
* **ChangeViewTo** - changes the current view type to the specified one. Possible view types include Day, Month, Timeline, Week and WorkWeek.
* **SelectInterval** - selects a specified interval on the scheduling timeline.
* **SetCurrentDate** - changes the current date to a specified one.

# [ETS](#tab/tabid-ets)

```ETS
*ExecuteTableAction
 CheckSelectedEventResources = Peter

*ExecuteTableAction
 CheckAppointmentType = ChangedOccurrence

*ExecuteTableAction
 ChangeViewTo = Timeline

*ExecuteTableAction
 SelectInterval = 08/12/2008 12:00;08/12/2008 13:00

*ExecuteTableAction
 SetCurrentDate = 10/27/2008
```

***

***

### FillRecord

Prefix: "*" and "!", Parameters: Primary and secondary.

Fills particular record fields with values via in-place editing. The following secondary parameters can be specified.

* **IdentityColumns** - optional. Specifies the columns used to identify the record where fields must be filled with values.
* **IdentityRow** - optional. Specifies the values corresponding to the columns specified by the **IdentityColumns** parameter. These values are used to identify a row by field values. You can pass "*" to this parameter to test the first available row. To test a row with a specific number, use a zero-based index (e.g Row[5] = _value_)
* **Columns** - required. Specifies the fields that must be filled with values.
* **Values** - required. Specifies the values that must be assigned to the fields.

If the **IdentityColumns** and **IdentityRow** parameters are not specified, the currently focused record is used.

# [ETS](#tab/tabid-ets)

```ETS
*FillRecord Contacts
 Columns = First Name, Address
 Values = Helen, '908 W.Capital Way'

!FillRecord Contacts
 IdentityColumns = First Name
 IdentityRow = John
 Columns = Last Name
 Values = Johnson
```

***

***

### ProcessRecord

Prefix: "*" and "!", Parameters: Primary and secondary.

Selects a record, and executes the specified Action on it. Secondary parameters specify record search criteria by providing field captions and corresponding values. The following additional secondary parameter can be specified.

* **Action** - optional. Specifies the Action to be performed on the selected record. If this parameter is not specified, the default Action is executed (normally, the Detail View is displayed for this record).

# [ETS](#tab/tabid-ets)

```ETS
*ProcessRecord
 User = Nataly
 Action = Delete
```

***

***

### SelectRecords

Prefix: "*", Parameters: Primary and secondary.

Selects specific records in a List View. An additional parameter's name specifies a column; its value specifies the value contained in this column. If there are selected rows before executing **SelectRecords**, then their selection persists. Use **UnselectRecords** to remove selection.

# [ETS](#tab/tabid-ets)

```ETS
*SelectRecords
 Columns = First Name
 Row = Mary
 Row = John
```

***

***

### UnselectRecords

Prefix: "*", Parameters: Primary and secondary.

Unselects specific records in a List View. An additional parameter's name specifies a column and its value specifies the value contained in this column.

# [ETS](#tab/tabid-ets)

```ETS
*UnselectRecords
 Columns = First Name
 Row = Mary
 Row = John
```

***

***

## File Operation Commands
These commands can be used when your application creates certain files in the file system (for example, performs data export) and you want to test this functionality.

***

### CheckFileExists

Prefix: "*" and "!", Parameters: Primary.

Checks the existence of the specified file.

# [ETS](#tab/tabid-ets)

```ETS
*CheckFileExists d:\tmp\Grid.pdf
```

***

***

### CompareFiles

Prefix: "*" and "!", Parameters: Secondary.

Compares the specified files. The Expected secondary parameter specifies the expected file. The Actual secondary parameter specifies the actual file.

# [ETS](#tab/tabid-ets)

```ETS
*ExecuteEditorAction Photo

*ExecuteEditorAction Photo(Save)

*FillForm
 File name: = c:\tmp\testphoto.jpg

*Action Save

*OptionalAction Yes

*Sleep 1000

*CompareFiles
 Expected = .\photo
 Actual = c:\tmp\testphoto.jpg
```

***

***

### CopyFile

Prefix: "*", Parameters: Secondary.

Copies the specified file. The SourceFileName secondary parameter specifies the source location. The DestFileName secondary parameter specifies the destination location.

# [ETS](#tab/tabid-ets)

```ETS
*CopyFile
 SourceFileName = d:\tmp\file1.txt
 Destination = d:\backup\file1.txt
```

***

***

### DeleteFile

Prefix: "*", Parameters: Primary.

Deletes the specified file.

# [ETS](#tab/tabid-ets)

```ETS
*DeleteFile d:\tmp\Grid.pdf
```

***

***

## Wildcards and Regular Expressions
You can use the question mark (**?**) and asterisk character (**&#0042;**) as wildcards in parameter values of the following commands.

[CheckActionsHint](#checkactionshint)

[CheckFieldValues](#checkfieldvalues)

[HandleDialog](#handledialog)

[CheckActionValue](#checkactionvalue)

[CheckValidationResult](#checkvalidationresult)

[CheckTable](#checktable)

[SelectRecords](#selectrecords)

[UnselectRecords](#unselectrecords)

[CheckTableSelection](#checktableselection)

The **?** wildcard substitutes for any one character, and **&#0042;** - for any zero or more characters.

# [ETS](#tab/tabid-ets)

```ETS
*CheckValidationResult
 Message = Data Validation Error:*
```

***

If you test a text that contains a question mark or asterisk characters, precede these symbols with a backslash symbol ("\").

# [ETS](#tab/tabid-ets)

```ETS
*HandleDialog
 Message = Do you want to cancel your changes\?
```

***
You can use [regular expressions](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) instead of wildcards to specify complex patterns in commands listed above. For this purpose, use the [SetStringCompareMode](#setstringcomparemode) command with the **Regex** parameter. To revert back to the wildcard mode, call **SetStringCompareMode** once again and pass **Wildcards** as the primary parameter.

For complete EasyTest sample scripts, refer to the following topics.

* [Test an Action](xref:113218)
* [Test Conditional Appearance Rules](xref:113345)
* [Test Validation Rules](xref:113294)

You can find more scripts in the **MainDemo** application shipped with XAF. The default location of this demos is _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_.
