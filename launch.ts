// w.ts
import { spawn } from "node:child_process";

if (Deno.args.length < 4) { 
  console.error("Usage: w.ts (wait_time) (m/s) (title) (command_to_execute)");
  Deno.exit(1);
}

const waitTime = Deno.args[0];
const unit = Deno.args[1];
let waitSeconds = 0;
if (unit === "m") {
  waitSeconds = parseInt(waitTime) * 60;
} else if (unit === "s") {
  waitSeconds = parseInt(waitTime);
} else {
  console.error(
    "Invalid time unit. Use 'm' (minutes) or 's' (seconds).",
  );
  Deno.exit(1);
}
const title = Deno.args[2];
const commandToExecute = Deno.args.slice(3);

const fullCommand = `echo waiting;sleep ${waitSeconds};echo started;${commandToExecute.join(" ")}`;

const cmd = spawn("xterm", [
  "-iconic",
  "-title",
  title,
  "-e",
  "sh",
  "-c",
  fullCommand,
], {
  detached: true,
});

cmd.unref();
Deno.exit(0);