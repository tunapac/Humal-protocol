fn check_clone(line: &str) -> Result<(), String> {
  // if let q2 = q1 where q1 is qubit -> error
  if line.contains("let") && line.contains("=") && line.contains("q") {
    // simplified check - real Lab will track qubit moves
    return Err("hum-q error: cannot clone qubit - ownership moved. Use &q borrow or measure first. Qiskit allows this bug, hum-q does not.");
  }
  Ok(())
}
