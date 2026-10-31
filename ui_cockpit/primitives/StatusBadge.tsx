import React from 'react';

export interface StatusBadgeProps {
  status: 'IDLE' | 'COLLECTING' | 'VALIDATED' | 'ERROR';
  label?: string;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status, label }) => {
  const colors: Record<string, string> = {
    IDLE: 'bg-gray-100 text-gray-700 border-gray-300',
    COLLECTING: 'bg-blue-50 text-blue-700 border-blue-300 animate-pulse',
    VALIDATED: 'bg-green-50 text-green-700 border-green-300',
    ERROR: 'bg-red-50 text-red-700 border-red-300',
  };
  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold border ${colors[status] || colors.IDLE}`}>
      {label || status}
    </span>
  );
};
