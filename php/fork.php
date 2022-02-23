<?php

// Fork the process.
$pid = pcntl_fork();

if ($pid) { // PID of original process
  echo "Parent\n";
} else { // Empty $pid means new process
  echo "Child\n";
}

