---
uid: "112576"
seealso:
- linkId: "112575"
title: Add Custom Log Entries and Customize the Default Tracer Behavior
---
# Add Custom Log Entries and Customize the Default Tracer Behavior

This topic describes the API you can use to add information to XAF [log files](xref:112575) from your code. The `DevExpress.Persistent.Base.Tracing` class is used for this purpose.

The `Tracing` class does not store log strings internally. It passes all strings to the [Trace.WriteLine](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.trace.writeline#System_Diagnostics_Trace_WriteLine_System_String_) method.

You can access the `Tracing` instance using the static `Tracing.Tracer` property and then call one of its methods.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
// ...
Tracing.Tracer.LogText("Some text");
```

***

## Tracing Methods
The following table list the most important methods of the `Tracing` class.

{|
|-

! Method
! Logged Information
! Sample Result
|-

| LogText(string text)
| The text passed as the method's parameter
| ``06.09.16 11:58:10.739  Text``
|-

| LogValue(string valueName, object objectValue)
| The caption and value passed as parameters, delimited by colon.
| ``06.09.16 11:58:10.739  ValueName: ObjectValue``
|-

| LogSeparator(string comment)
| The text passed as the method's parameter, and a separator under it.
| ``06.09.16 11:58:10.739 Comment``

``06.09.06 11:58:10.739 ====================``
|-

| LogSubSeparator(string comment)
| The separator and then the text passed as the value parameter.
| ``06.09.16 11:58:10.739 --------------``

``06.09.06 11:58:10.739 Comment``
|-

| LogError(Exception exception)
| The type and message of the specified exception, followed by the stack trace.
| ``The error that occurred``

``Type: Exception type``

``Message: Exception message``

``Stack trace: ...``
|}

## Custom Tracing

You can inherit the `Tracing` class and override its virtual methods to implement custom logging.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
// ...
public class MyTracing : Tracing {
    public override void LogError(Exception exception) {
        // Implement custom logging for exceptions here.
    }
    // You can also override other virtual methods of Tracing 
}
```

***
The static `Tracing.CreateCustomTracer` event occurs when the `Tracing.Tracer` instance is initialized. Handle this event to replace the default `Tracing` instance with a custom instance.
If you call the `Tracing.Initialize` method, handle the `Tracing.CreateCustomTracer` event before the `Tracing.Initialize` method call.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
using System.Diagnostics;
// ...
Tracing.CreateCustomTracer += delegate(object s, CreateCustomTracerEventArgs args) {
    args.Tracer = new MyTracing();
};
// ...
Tracing.Initialize((int)TraceLevel.Info);
//...
```

***

You can handle the `Tracing.CreateCustomTracer` event in the `Main` method of the Windows Forms application located in the _Program.cs_ file, before the `Tracing.Initialize` method call;
